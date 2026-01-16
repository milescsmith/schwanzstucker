# boilerplate for typer-based cli
# be a lot nicer if typer just had API-based documentation instead
# of the tutorial-style that is the only thing available

from typing import Annotated
import typer
from enum import StrEnum, IntEnum, Enum

class OptionsForThings(StrEnum): # equivalent to OptionsForThings(Enum, str)
    OPTION_ONE = "option.one"
    OPTION_TWO = "option.two"
    # OptionsForThings.OPTION_ONE == "option.one"

class IntOptions(IntEnum):
    INT_OPTION_ONE = 1
    INT_OPTION_TWO = 2

subcommand_one = typer.Typer(
    name="Main App Subcommand One",
    help=(
        "IT DOES STUFF!"
    ),
    add_completion=False,
    no_args_is_help=True,
    add_help_option=True,
)

subcommand_two = typer.Typer(
    name="Main App Subcommand Two",
    help=(
        "IT DOES THINGS!"
    ),
    add_completion=False,
    no_args_is_help=True,
    add_help_option=True,
)

main_app = typer.Typer(
    name="10X processing script generator",
    help=(
        "Create the scripts necessary to process raw sequencing data coming from 10X Genomics assays "
        "into count matrices"
    ),
    add_completion=False,
    no_args_is_help=True,
    add_help_option=True,
)
main_app.add_typer(
    typer_instance=subcommand_one,
    name="subcommand1",
    no_args_is_help=True,
    help=(
        "A subcommand."
    ),
)
main_app.add_typer(
    typer_instance=subcommand_two,
    name="subcommand2",
    no_args_is_help=True,
    help="Another, different subcommand",
)

def version_callback(version: Annotated[bool, typer.Option("--version")] = True) -> None:  # FBT001
    """Prints the version of the package."""
    if version:
        rprint(f"[yellow]asapseq-script-gen[/] version: [bold blue]{__version__}[/]")
        raise typer.Exit()


@main_app.callback()
def version_callback(
    version: Annotated[
        bool,
        typer.Option(
            "-v",
            "--version",
            help="Show Cassini version",
        ),
    ] = False,
) -> None:  # FBT001
    """Prints the version of the package."""
    if version:
        rprint(f"[yellow]cassini[/] version: [bold blue]{__version__}[/]")
        raise typer.Exit()


@main_app.callback()
def verbosity_callback(
    verbose: Annotated[
        int,
        typer.Option(
            "-l",
            "--verbose",
            help="Control output verbosity. Pass this argument multiple times to increase the amount of output.",
            count=True,
        ),
    ] = 0,
    version: Annotated[
        bool, typer.Option("-v", "--version", help="Show Cassini version", callback=version_callback)
    ] = False,
) -> None:
    verbosity_level = verbose  # noqa: F841


@main_app.command
def main(
    param1: Annotated[
        OptionsForThings, typer.Option(
            "--param1",
            "-p",
            help="the thing to do",
        )
    ],
    param2: Annotated[
        int, typer.Option(
            "--param2",
            "-q",
            min=1,
            max=10,
            clamp=True,
            help="how many times to do that thing"
        )
    ],
    version: Annotated[
        bool, typer.Option("--version", help="Show version", callback=version_callback, is_eager=True)
    ] = False,
):
    pass


@subcommand_one.command()
def sub1():
    pass

@subcommand_two.command
def sub2():
    pass