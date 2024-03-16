import json

def list_vidoes(vidoe_data):
    for index,video in enumerate(vidoe_data, start=1):
        print(f"{index} : {video['name']} - {video['time']}")
    print(" ")


def add_video(video_data):
    name = input("Enter name: ")
    time = input("Enter time: ")
    video_data.append({"name":name, "time": time})
    save_vidoes(video_data)


def update_video(vidoe_data):
    list_vidoes(vidoe_data)
    print(" ")
    index = int(input("Enter video number to update: "))
    if 1<= index <= len(vidoe_data):
        name = input("Enter name: ")
        time = input("Enter time: ")
        vidoe_data[index-1] = {'name': name , 'time':time}
        save_vidoes(vidoe_data)
    else:
        print("Invalid index selected")



def delete_video(video_data):
    list_vidoes(video_data)
    print(" ")
    index = int(input("Enter video number to delete: "))
    if 1<= index <= len(video_data):
        del video_data[index-1]
        save_vidoes(video_data)
    else:
        print("Invalid index selected")


def load_videos():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_vidoes(vidoe_data):
    with open('youtube.txt','w') as file:
        json.dump(vidoe_data,file)


def main():
    while True :
        video_data = load_videos()
        print(" ")
        print(" Youtube Manager | Choose an option ")
        print(" 1 - Listing videos")
        print(" 2 - Adding video")
        print(" 3 - Update video")
        print(" 4 - Delete video")
        print(" 5 - Exit app")
        choice = input("Enter choice : ")
        print(" ")
        match choice:
            case '1':
                list_vidoes(video_data)
            case '2':
                add_video(video_data)
            case '3':
                update_video(video_data)
            case '4':
                delete_video(video_data)
            case '5':
                break
            case _:
                print("Enter correct choice : ")
        

if __name__ == '__main__':
    main()
