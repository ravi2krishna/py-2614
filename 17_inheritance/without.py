# WithOut Inheritance - We Write Same Functionalities Again and Again For Multiple Times 

# LMS Application (Application For Watching Course Videos)

# Students      ->  Watch Videos

# VideoAdmin    ->  Watch Videos & Add Videos 

# SuperAdmin    ->  Watch Videos, Add Videos & Delete Videos 

class Student:
    # Watch Videos 
    def watch_videos(self):
        print("=" * 50)
        print("Functionality For Watching Videos")
        print("=" * 50)
        print("W")
        print("A")
        print("T")
        print("C")
        print("H")
        print("I")
        print("N")
        print("G")
        print("V")
        print("I")
        print("D")
        print("E")
        print("O")
        print("..............") # Real World Code is like 5000 lines of code 
        
        
class VideoAdmin:
    # Watch Videos 
    def watch_videos(self):
        print("=" * 50)
        print("Functionality For Watching Videos")
        print("=" * 50)
        print("W")
        print("A")
        print("T")
        print("C")
        print("H")
        print("I")
        print("N")
        print("G")
        print("V")
        print("I")
        print("D")
        print("E")
        print("O")
        print("..............") # Real World Code is like 5000 lines of code 
        
    # Add Videos 
    def add_videos(self):
        print("=" * 50)
        print("Functionality For Adding Videos")
        print("=" * 50)
        print("A")
        print("D")
        print("D")
        print("I")
        print("N")
        print("G")
        print("V")
        print("I")
        print("D")
        print("E")
        print("O")
        print("..............") # Real World Code is like 5000 lines of code 


class SuperAdmin:
    # Watch Videos 
    def watch_videos(self):
        print("=" * 50)
        print("Functionality For Watching Videos")
        print("=" * 50)
        print("W")
        print("A")
        print("T")
        print("C")
        print("H")
        print("I")
        print("N")
        print("G")
        print("V")
        print("I")
        print("D")
        print("E")
        print("O")
        print("..............") # Real World Code is like 5000 lines of code 
        
    # Add Videos 
    def add_videos(self):
        print("=" * 50)
        print("Functionality For Adding Videos")
        print("=" * 50)
        print("A")
        print("D")
        print("D")
        print("I")
        print("N")
        print("G")
        print("V")
        print("I")
        print("D")
        print("E")
        print("O")
        print("..............") # Real World Code is like 5000 lines of code 
        
    # Delete Videos 
    def delete_videos(self):
        print("=" * 50)
        print("Functionality For Deleting Videos")
        print("=" * 50)
        print("D")
        print("E")
        print("L")
        print("E")
        print("T")
        print("I")
        print("N")
        print("G")
        print("V")
        print("I")
        print("D")
        print("E")
        print("O")
        print("..............") # Real World Code is like 5000 lines of code 
        
        # Now Technically We Have 30k lines of Code - Duplicated Code is 15k lines i.e 50% is Duplicate Code 
    
print("Student User")
student_user = Student()
student_user.watch_videos()

print("Video Admin User")
video_admin_user = VideoAdmin()
video_admin_user.watch_videos()
video_admin_user.add_videos()

print("Super Admin User")
super_admin_user = SuperAdmin()
super_admin_user.watch_videos()
super_admin_user.add_videos()
super_admin_user.delete_videos()