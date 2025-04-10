# server.py

from mcp.server.fastmcp import FastMCP,Context
from pydantic import AnyUrl, Field

from typing import List, Union
import httpx
import json
import os
import sys
from loguru import logger
from utils.data_reader import db_search_booking
# This is the shared MCP server instance
mcp = FastMCP("ohana_server",
              dependencies=[
                'pydantic',
                'pymysql',
                'httpx',
                'beautifulsoup4',
    ],
    log_level='DEBUG',
              )

# Set up logging
logger.remove()
logger.add(sys.stderr, level=os.getenv('FASTMCP_LOG_LEVEL', 'WARNING'))



@mcp.tool()
def get_booking(
    ctx: Context,
    #search_phrase: str = Field(description='Search phrase to use'),
    booking_number: str = Field(description='Search by booking number'),    
    limit: int = Field(
        default=10,
        description='Maximum number of results to return',
        ge=1,
        le=50,
    ),
) -> str :
    """Search booking by Search API.

    ## Usage

    This tool searches across all gates bookings. 

    ## Search Tips

    ## Result Interpretation
   

    ## Follow-up Actions
    

    Args:
        ctx: MCP context for logging and error handling
        booking_number: booking number to search hotel booking        
        limit: Maximum number of results to return

    Returns:
        str: JSON string of search results
    """
    logger.debug(f'Searching booking for: {booking_number} ')

    if(not booking_number):
        raise ValueError("Please provide booking number .")
    
    data = []
    
    data = db_search_booking(booking_number)
   
    logger.debug(f'Found {len(data)} search results for: {booking_number}')
    #return "\n create user = ".join(sql in data if sql else "No results found")
    return json.dumps(data, default=str)



# Entry point to run the server
if __name__ == "__main__":
     mcp.run()