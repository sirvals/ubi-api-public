from fastapi import FastAPI
import uvicorn
import ubi_player

app = FastAPI()

@app.get("/pc/{username}")
async def search_pc(username: str):
    """
    Search for a player on PC using their Ubisoft username.
    
    Parameters:
        username (str): The Ubisoft username to search for.
        
    Returns:
        dict: A dictionary containing the player's profile information.
    """
    response = await ubi_player.player_search(username)
    return response

@app.get("/xbox/{username}")
async def search_xbox(username: str):
    """
    Search for a player on Xbox using their Ubisoft username.
    
    Parameters:
        username (str): The Ubisoft username to search for.
        
    Returns:
        dict: A dictionary containing the player's profile information.
    """
    response = await ubi_player.player_search(username,"xbl")
    return response

@app.get("/psn/{username}")
async def search_psn(username: str):
    """
    Search for a player on Playstation using their Ubisoft username.
    
    Parameters:
        username (str): The Ubisoft username to search for.
        
    Returns:
        dict: A dictionary containing the player's profile information.
    """
    response = await ubi_player.player_search(username,"psn")
    return response

@app.get("/")
async def contact():
    """
    Get the contact information for the developer.
    
    Returns:
        dict: A dictionary containing the contact information.
    """
    return{"discord":"ideals#5281"}

if __name__ == "__main__":
    uvicorn.run(app, host="185.10.68.89", port=80)
