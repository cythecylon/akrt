# akrt
## About
Simple robust repair tracker based on using text files. 

Runs simple http webserver to inform customer of ticket status.

## Dependencies
* Python 3.6.1 required to use Pathlib
* Flask

## Usage

### Create New Ticket
`akrt.py new`

### Update Ticket
`akrt.py update <ticketid>`

### Read Ticket
`akrt.py about <ticketid>`

### Launch Web Server
`akrt.py daemon`
