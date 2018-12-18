import news_fetcher
import video_generator
import yt_uploader


def main():
    news_fetcher.main()
    video_generator.main()
    yt_uploader.main()


if __name__ == '__main__':
    main()
