import instaloader
from datetime import timedelta


class Instagram:
    """
    this class is analyse instagram
    """
    def __init__(self):
        pass

    def get_user_name(self, username: str):
        """
        this function is take an username from the input in the GUI and put it in the right format in the instagram to get information
        :param username: is the param that we get from the GUI input to the profile we need to build
        :return:  access to scrape an information from Instagram
        """
        Instagram_object = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(Instagram_object.context, username)
        return profile

    def get_access_to_post(self, shortcode: str):
        """
        this function will be use in every part of using post information
        :param shortcode: its some code that every post has like the id's of the code
        :return: give me access to the information in the post
        """
        L = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(L.context, shortcode=shortcode)
        return post

    def get_number_of_follower(self, username: str) -> int:
        """
        this function will return the number of followers on the input username
        :param username: is the param that we get from the GUI input to the profile we need to build
        :return: the number of followers for this username
        """

        current_profile = self.get_user_name(username=username)

        return current_profile.followers

    def get_number_of_followees(self, username) -> int:
        """
        this function will return the number oif followees that this username follow about the input username
        :param username:  is the param that we get from the GUI input to the profile we need to build
        :return: the number of followees that username is follow
        """
        current_profile = self.get_user_name(username=username)

        return current_profile.followees

    def get_analysis_of_biography(self, username):
        """
        this function is analyse biography of people and scrape information about them just from the biography
        :param username: is the param that we get from the GUI input to the profile we need to build
        :return: will return pieces of data about this parson and we will add this data to the profile that we will build
        """

        file_base_of_biograph_path = "Words_base_of_biography.txt"
        current_profile = self.get_user_name(username=username)
        the_actual_biography = current_profile.biography.split()

        with open(file_base_of_biograph_path, 'r', encoding='utf-8') as opening_a_file:
            data_of_biography = opening_a_file.readlines()
            updating_data_of_biography = [word.strip() for word in data_of_biography]

            for comparing_words in the_actual_biography:
                if comparing_words in updating_data_of_biography:
                    print(comparing_words)
                else:
                    new_word = comparing_words[0].upper()
                    if new_word in updating_data_of_biography:
                        print(new_word)
                    else:
                        new_word_2 = comparing_words + "s"
                        if new_word_2 in updating_data_of_biography:
                            print(new_word_2)

    def get_frequency_uploading_posts(self, username: str) -> dict:

        """
        this function checking the frequency of uploading posts about some person we,
         check the difference of the date and time between the posts dates and return the average of uploading posts
        :param username: is the param that we get from the GUI input to the profile we need to build
        :return: dictionary of data about the average of the uploading posts,
         and the numbers of posts that this person have in his account and the average of the differencces
        """

        current_profile = self.get_user_name(username=username)

        date_strings = []
        for post in current_profile.get_posts():
            caption = post.caption
            post_date_utc = post.date_utc
            if caption:
                date_strings.append(post_date_utc)

        time_differences = [date_strings[i] - date_strings[i - 1] for i in range(1, len(date_strings))]

        total_time_difference = sum(time_differences, timedelta())

        average_time_difference = total_time_difference / len(
            time_differences) if time_differences else timedelta()

        average_time_per_post = average_time_difference / len(time_differences) if len(
            time_differences) > 0 else timedelta()
        current_data = {
            "total posts": len(date_strings),
            "the difference time": total_time_difference,
            "the average of time difference": average_time_difference,
            "the average time between posts": average_time_per_post
        }

        return current_data

    def get_number_of_likes_per_post(self, shortcode: str) -> int:
        """
        this function will give me the num of like that this post have in thez present
        :param shortcode: its some code that every post has like the id's of the code
        :return: the num of likes on the current post
        """
        current_post = self.get_access_to_post(shortcode=shortcode)

        return current_post.likes

    def get_list_of_shortcode(self, username: str) -> list:
        """
        this function is return the shortcode that every post have to get another function in instaloader library
        :param username: shortcode: its some code that every post has like the id's of the code
        :return: list of shortcodes in any input username
        """
        current_profile = self.get_user_name(username=username)

        data_of_shortcode = [str(post) for post in current_profile.get_posts()]
        update_data_of_shortcode = [shortcode.strip().split()[1][:-1] for shortcode in data_of_shortcode]

        return update_data_of_shortcode

    def get_num_of_comments(self, shortcode: str) -> int:
        """
        this function is return the number of comments by post
        :param shortcode: shortcode: its some code that every post has like the id's of the code
        :return: the number of comments
        """
        current_shortcode = self.get_access_to_post(shortcode=shortcode)

        return current_shortcode.comments

    def get_sum_of_likes_per_username(self, username):
        """
        this function is sum all the likes on the username and return us the sum of everything
        :param username: is the param that we get from the GUI input to the profile we need to build
        :return: the sum of likes on specific username
        """
        sum_of_likes = 0
        shortcods_list = self.get_list_of_shortcode(username=username)
        for shortcode in shortcods_list :
            sum_of_likes += self.get_number_of_likes_per_post(shortcode=shortcode)
        return sum_of_likes


if __name__ == "__main__":
    instagram = Instagram()
    print(instagram.get_frequency_uploading_posts("adi.evran"))