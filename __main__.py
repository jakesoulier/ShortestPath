# from connection.game.directing.director import Director
from game.services.video_service import VideoService
# from game.services.keyboard_service import KeyboardService
from game.directing.director import Director
from game.casting.cast import Cast
from game.casting.walls import Wall

def main():
    
    # create Cast
    cast = Cast()
    cast.add_actor('wall', Wall())
    
    # keyboard_service = KeyboardService()
    video_service = VideoService()
    
    director = Director(video_service)
    director.start_game(cast)
    
    
    
if __name__ == "__main__":
    main()