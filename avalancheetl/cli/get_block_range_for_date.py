# MIT License
# Modifications Copyright (c) Zhassulan Shaikhygali, shaikh.zhas@gmail.com
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import click

from datetime import datetime
from avalancheetl.web3_utils import build_web3

from blockchainetl.file_utils import smart_open
from blockchainetl.logging_utils import logging_basic_config
from avalancheetl.service.ava_service import AvaService
from avalancheetl.providers.auto import get_provider_from_uri
from avalancheetl.utils import check_classic_provider_uri

logging_basic_config()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-p', '--provider-uri', required = True, type=str, help='The URI of the web3 provider e.g. ')
@click.option('-d', '--date', required=True, type=lambda d: datetime.strptime(d, '%Y-%m-%d'),
              help='The date e.g. 2018-01-01.')
@click.option('-o', '--output', default='block_range.txt', show_default=True, type=str, help='The output file. If not specified stdout is used.')
@click.option('-c', '--chain', default='avalanche', show_default=True, type=str, help='The chain network to connect to.')
def get_block_range_for_date(provider_uri, date, output, chain='avalanche'):
    """Outputs start and end blocks for given date."""
    provider_uri = check_classic_provider_uri(chain, provider_uri)
    provider = get_provider_from_uri(provider_uri)
    web3 = build_web3(provider)
    ava_service = AvaService(web3)
    start_block, end_block = ava_service.get_block_range_for_date(date)

    with smart_open(output, 'w') as output_file:
        output_file.write('{},{}\n'.format(start_block, end_block))
