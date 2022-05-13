#!/usr/bin/env python
""" any2tsv: Convert various bioinformatic outputs to TSV """

from rich import print
import csv
import rich_click as click
import rich.table
import os
import sys

import any2tsv
import any2tsv.parsers

# Set up nicer formatting of click cli help messages
click.rich_click.MAX_WIDTH = 100
click.rich_click.USE_RICH_MARKUP = True

def rich_force_colors():
    """
    Check if any environment variables are set to force Rich to use coloured output

    Borrowed from nf-core/tools (lots of "rich/click" gold mines)
    https://github.com/nf-core/tools/blob/master/nf_core/utils.py
    """
    if os.getenv("GITHUB_ACTIONS") or os.getenv("FORCE_COLOR") or os.getenv("PY_COLORS"):
        return True
    return None

@click.command(context_settings=dict(help_option_names=["-h", "--help"]), no_args_is_help=True)
@click.version_option(any2tsv.__version__)
@click.argument("tool_name", metavar="<tool name>", required=False)
@click.argument("input_file", metavar="<input file>", required=False)
@click.option('-l', '--list_parsers', is_flag=True, default=False, help="List tools with an available parser.")
@click.option("-s", "--sample", type=str, default=None, help="ID to use for the 'any2tsv_id' column. (Default: input file name)")
def run_any2tsv(tool_name, input_file, list_parsers, sample):
    if list_parsers:
        print_parsers(any2tsv.parsers.__all__)
    
    if not tool_name and not input_file:
        raise click.ClickException("Please specify a tool name and input file.")

    tool_fname = tool_name.replace("-", "_")
    any2tsv_id = sample if sample else os.path.basename(input_file)
    if tool_fname in any2tsv.parsers.__all__:
        data_dict = getattr(any2tsv.parsers, tool_fname).parse(input_file, any2tsv_id)
        dict_writer = csv.DictWriter(sys.stdout, data_dict.keys(), delimiter='\t')
        dict_writer.writeheader()
        dict_writer.writerow(data_dict)
    else:
        raise click.ClickException(f"'{tool_name}' is not available. use --list_parsers to see parsable tool outputs.")


def print_parsers(parsers) -> None:
    """
    Print a list of parsable tool outputs.
    """
    stderr = rich.console.Console(stderr=True, force_terminal=rich_force_colors())
    table = rich.table.Table()
    table.title = "\n".join([
        "",
        f"any2tsv (v{any2tsv.__version__}) - Convert various bioinformatic outputs to TSV",
        "",
        f"[bold yellow]Usage:[/] [bold]any2tsv [OPTIONS][/] [bold yellow]<parser name> <input file>[/]",
        ""
    ])
    table.title_style = rich.style.Style()
    table.add_column(f"Parsers ({len(parsers)})", style="green")
    table.add_column("Description", justify="right")
    for parser in parsers:
        rowdata = [
            f"{getattr(any2tsv.parsers, parser).__name__}",
            f"{getattr(any2tsv.parsers, parser).__description__}"
        ]
        table.add_row(*rowdata)
    stderr.print(table)
    sys.exit(0)

# Main script is being run - launch the CLI
if __name__ == "__main__":
    run_any2tsv()
