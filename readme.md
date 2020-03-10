## Find out how many transactions are ahead of you

The [Bitcoinfees](https://bitcoinfees.earn.com/) site offers an API that returns a JSON structure summarising the number of Bitcoin transactions that are currently sitting in the mempool unprocessed.

This script takes a command line parameter - the number of satoshis/byte - and calls the Bitcoinfees API to calculate and return the number of transactions that are offering higher fees in order to be processed, and the number of transactions that are offering the same or higher fees.

#### To install:  
Run `sudo ./install.sh` to create a Python venv with all the required dependencies. Or if you don't like using sudo, look at the script and enter the commands manually yourself.

#### Usage

Run `./run.sh <satoshis/byte>`

#### Warning

I put this together in about 15 minutes, so there's minimal error checking. YMMV.
