import click
import json
import sys
import typing

from dcso_converter.converter import DCSOConverter


def parse_madmp(ctx, param, value: typing.IO) -> dict:
    # TODO: some validation against schema? minimal required attributes?
    return json.load(value)


@click.command(name="dcso_converter")
@click.argument('input', type=click.File('r', encoding='utf-8'), callback=parse_madmp)
@click.argument('output', type=click.File('w'), default=sys.stdout)
@click.option('-f', '--format', type=click.Choice(DCSOConverter.FORMATS), default='ttl')
def main(input: dict, output: typing.IO, format: str):
    converter = DCSOConverter()
    result = converter.convert(input, format)
    if isinstance(result, (bytes, bytearray)):
        result = result.decode(sys.stdout.encoding)
    output.write(result)
