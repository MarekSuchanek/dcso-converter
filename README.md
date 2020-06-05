# dcso-converter

A tool for conversions between [maDMP in JSON](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard) and [DCSO](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard/tree/master/ontologies)

## Requirements

* Python 3.5+

## Usage

1. Set up and use virtual env (optional): ``python3 -m venv env && source env/bin/activate``
2. Install: ``pip install -e .``
3. Run: ``dsco_converter mydmp.json`` or as filter ``cat mydmp.json | dsco_converter - | tee mydmp.ttl``
4. Find our more options ``dsco_converter --help``

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for more details.
