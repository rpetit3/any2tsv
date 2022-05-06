#!/usr/bin/env python
""" any2tsv: Convert various bioinformatic outputs to TSV """

from rich import print
import csv
import rich_click as click
import sys

import any2tsv
import any2tsv.tools

# Set up nicer formatting of click cli help messages
click.rich_click.MAX_WIDTH = 100
click.rich_click.USE_RICH_MARKUP = True

@click.command(context_settings=dict(help_option_names=["-h", "--help"]), no_args_is_help=True)
@click.version_option(any2tsv.__version__)
@click.argument("tool_name", metavar="<tool name>", required=False)
@click.argument("input_file", metavar="<input file>", required=False)
@click.option('--list_tools', is_flag=True, default=False, help="List tools with an available parser.")
def run_any2tsv(tool_name, input_file, list_tools):
    if list_tools:
        click.echo("Print all available tools.")
        print(any2tsv.tools.__all__)

    
    if not tool_name and not input_file:
        raise click.ClickException("Please specify a tool name and input file.")

    tool_fname = tool_name.replace("-", "_")
    if tool_fname in any2tsv.tools.__all__:
        data_dict = getattr(any2tsv.tools, tool_fname).parse(input_file)
        dict_writer = csv.DictWriter(sys.stdout, data_dict.keys(), delimiter='\t')
        dict_writer.writeheader()
        dict_writer.writerow(data_dict)
    else:
        raise click.ClickException(f"'{tool_name}' is not available. use --list_tools to see available tools.")

# Main script is being run - launch the CLI
if __name__ == "__main__":
    run_any2tsv()
