""" The main entrypoint for the application. """
import logging

# Set up logging
logging.basicConfig(filename='gpt_dungeon_master.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def hello_world() -> str:
    """ Returns a friendly greeting. """
    return "Hello World!"
