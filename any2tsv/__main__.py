#!/usr/bin/env python
""" any2tsv: Convert various bioinformatic outputs to TSV """

from rich import print
import csv
import rich_click as click
import rich.console
import rich.table
import sys

import any2tsv
import any2tsv.parsers

# Set up nicer formatting of click cli help messages
click.rich_click.MAX_WIDTH = 100
click.rich_click.USE_RICH_MARKUP = True

@click.command(context_settings=dict(help_option_names=["-h", "--help"]), no_args_is_help=True)
@click.version_option(any2tsv.__version__)
@click.argument("tool_name", metavar="<tool name>", required=False)
@click.argument("input_file", metavar="<input file>", required=False)
@click.option('--list_parsers', is_flag=True, default=False, help="List tools with an available parser.")
def run_any2tsv(tool_name, input_file, list_parsers):
    if list_parsers:
        print_parsers(any2tsv.parsers.__all__)

    
    if not tool_name and not input_file:
        raise click.ClickException("Please specify a tool name and input file.")

    tool_fname = tool_name.replace("-", "_")
    if tool_fname in any2tsv.parsers.__all__:
        data_dict = getattr(any2tsv.parsers, tool_fname).parse(input_file)
        dict_writer = csv.DictWriter(sys.stdout, data_dict.keys(), delimiter='\t')
        dict_writer.writeheader()
        dict_writer.writerow(data_dict)
    else:
        raise click.ClickException(f"'{tool_name}' is not available. use --list_parsers to see parsable tool outputs.")


def print_parsers(parsers) -> None:
    """
    Print a list of parsable tool outputs.
    """
    table = rich.table.Table()
    table.title = f"""
    any2tsv (v{any2tsv.__version__}) - Convert various bioinformatic outputs to TSV

    [bold yellow]Usage:[/bold yellow] [bold]any2tsv [OPTIONS][/bold] [bold yellow]<tool name> <input file>[/bold yellow]
    """
    table.title_justify = "left"
    table.add_column("Tool Name", style="green")
    table.add_column("Description", justify="right")
    for parser in parsers:
        rowdata = [
            f"{getattr(any2tsv.parsers, parser).__name__}",
            f"{getattr(any2tsv.parsers, parser).__description__}"
        ]
        table.add_row(*rowdata)
    print(table)
    sys.exit(0)

# Main script is being run - launch the CLI
if __name__ == "__main__":
    run_any2tsv()
