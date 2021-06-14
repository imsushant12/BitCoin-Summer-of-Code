# BitCoin Summer of Code challenge Solution.
Bitcoin miners construct blocks by selecting a set of transactions from their mempool. Each transaction in the mempool:
- includes a fee which is collected by the miner if that transaction is included in a block
- has a weight , which indicates the size of the transaction
- may have one or more parent transactions which are also in the mempool

The miner selects an ordered list of transactions which have a combined weight below the maximum block weight. Transactions with parent transactions in the
mempool may be included in the list, but only if all of their parents appear before them in the list.<br>
Naturally, the miner would like to include the transactions that maximize the total fee.<br>
Your task is to write a program which reads a file mempool.csv, with the format:
<txid>,<fee>,<weight>,<parent_txids>
- txid is the transaction identifier
- fee is the transaction fee
- weight is the transaction weight
- parent_txids is a list of the txids of the transaction’s unconfirmed parent transactions (confirmed parent transactions are not included in this list).<br>
  
The output from the program should be txids, separated by newlines, which make a valid block, maximizing the fee to the miner. Transactions MUST appear in order
(no transaction should appear before one of its parents).
