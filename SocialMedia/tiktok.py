import sys

import requests
from bs4 import BeautifulSoup


class TikTok:
    """

    """

    def get_access_with_username(self, username):
        """

        :param username:
        :return:
        """
        url = f"https://www.tiktok.com/@{username}"

        response = requests.get(url)

        return response

    def get_number_of_followers(self, username):
        """
        this function is return the number of the fullowers that this username is have
        :param username: is the param that we get from the GUI input to the profile we need to build
        :return: the number of the followers that this username has in his account
        """
        if self.get_access_with_username(username=username).status_code == 200:
            soup = BeautifulSoup(self.get_access_with_username(username=username).text, "lxml")

            element_with_class = soup.find('strong', title="Followers")

            if element_with_class:
                followers_count = element_with_class.text
                if 'M' in followers_count:
                    update_followers_count = int(float(followers_count[0:len(followers_count) - 1]) * 1000000)
                    return update_followers_count
                elif 'K' in followers_count:
                    update_followers_count = int(float(followers_count[0:len(followers_count) - 1]) * 1000)
                    return update_followers_count
                else:
                    return followers_count
        else:
            print("Faild to retrieve the web page. ")

    def tikTot_(self):
        for i in range(10):
            print(f"\033[91mSyntaxError: invalid syntax. tiktot can't use the followers method anymore. line {i + 25} \033[0m")
        sys.exit()

    def get_number_of_followees(self, username):
        """
        this function will return the number oif followees that this username follow about the input username
        :param username:  is the param that we get from the GUI input to the profile we need to build
        :return: the number of followees that username is follow
        """
        if self.get_access_with_username(username=username).status_code == 200:
            soup = BeautifulSoup(self.get_access_with_username(username=username).text, "lxml")

            followees_count = soup.find('strong',title="Following")

            if followees_count:
                followers_count = followees_count.text
                if 'M' in followers_count:
                    update_followees_count = int(float(followers_count[0:len(followers_count) - 1]) * 1000000)
                    return update_followees_count
                elif 'K' in followers_count:
                    update_followees_count = int(float(followers_count[0:len(followers_count) -1]) * 1000)
                    return update_followees_count
                else:
                    return followers_count
        else:
            print("Faild to retrieve the web page. ")

    def sum_of_likes_per_username(self,username):
        """
        this function is sum all the likes on the username and return us the sum of everything
        :param username: is the param that we get from the GUI input to the profile we need to build
        :return: the sum of likes on specific username
        """
        if self.get_access_with_username(username=username).status_code == 200:
            soup = BeautifulSoup(self.get_access_with_username(username=username).text,"lxml")

            sum_of_likes = soup.find('strong',title="Likes")

            if sum_of_likes:
                sum_of_likes = sum_of_likes.text
                if 'M' in sum_of_likes :
                    update_sum_of_likes = int(float(sum_of_likes[0:len(sum_of_likes) - 1]) * 1000000)
                    return update_sum_of_likes
                elif 'K' in sum_of_likes:
                    update_sum_of_likes = int(float(sum_of_likes[0:len(sum_of_likes) - 1]) * 1000)
                    return update_sum_of_likes
                else:
                    return sum_of_likes
        else:
            print("Faild to retrieve the web page. ")

    def list_of_ids_for_posts(self, username):
        """

        :param username:
        :return:
        """
        if self.get_access_with_username(username=username).status_code == 200:
            soup = BeautifulSoup(self.get_access_with_username(username=username).text,"lxml")

            video_ids = soup.find_all(class_="e1cg0wnj1")

            list_of_ids = [element for element in video_ids]

            return list_of_ids
        else:
            print("Faild to retrieve the web page. ")





if __name__ == "__main__":
    tiktok = TikTok()
    print(tiktok.list_of_ids_for_posts("emroume_elalem3"))
