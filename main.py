import get_the_img_ready
import quote
import get_links
import save_img
import bot
import time

def main():
    # save the links in txt file
    get_links.save_the_link()

    # save the image downlaoded from the link
    save_img.save_img()
    
    # write the quote by fetching it 
    get_the_img_ready.write_on_image(quote.get_quote()[1])
    
    #start the bot
    bot.start_bot('img_with_quotes.jpg',quote.get_quote()[0])
    
if __name__ == '__main__':
    while True:
        main()
        time.sleep(60*60)