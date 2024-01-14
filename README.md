# MeowBot
MeowBot is a robot in a video of a cute cat who teaches how to teach children in preschool institutions and increase their interest in learning. The use of Meowbot robots in preschool institutions will improve the efficiency of mastering information content, increase motivation to study and physical activity, thanks to the interactive form of classes.

# Full description of the project

## Problem
     
The key problem in preschool education is adapting to the different thinking patterns of modern children, necessitating innovative teaching methods and technologies. Additionally, addressing staffing shortages through the integration of information technologies can enhance the effectiveness and engagement of the educational process.
    
## Project topic
     
Robot-based education for preschool children aims to enhance their skills and abilities in mathematics, language, social, and cognitive domains by assessing individual needs and utilizing interactive methods. This involves the establishment of a unified educational and gaming environment, in conjunction with teachers and parents, to optimize children's developmental conditions.

## Assessment of the current state of the problem being solved.
     
1) Early childhood is a pivotal period for a child's brain development, leading to a growing emphasis on the education and nurturing of children in preschools.

2) Contemporary educational programs in preschool institutions encompass vital components, including social, emotional, cognitive, and physical development.

3) Modern kindergartens also incorporate digital technologies, such as educational tablet games, to facilitate multifaceted child development.

4) One of the primary objectives of preschool institutions is fostering children's social and communication skills. Kindergartens now actively employ games and exercises to enhance communication abilities, cooperation, and empathy.

5) Encouraging the creative potential of children involves the utilization of various techniques and technologies aimed at nurturing their imagination, fantasy, and creative activities.

    
## Description of the robot
   
Meowbot is a unique device designed to help children develop. The robot can display tasks on a tablet and ask children for colors, numbers, letters of the alphabet, shapes of figures, and reproduce other tasks.

| ![Meowbot Image 1](https://github.com/hlopushkaa/photomeowbot/blob/main/afd.jpg) | ![Meowbot Image 2](https://github.com/hlopushkaa/photomeowbot/blob/main/adf2.jpg) |
| --- | --- |

Children can engage with the robot across various subjects, receiving feedback on their answers. Correct responses earn praise, while incorrect ones are explained and corrected. Additionally, the robot leads physical warm-up sessions every 15-20 minutes, incorporating dance and movement. It can also provide entertainment, play music, and adapt to each child's specific needs, making learning interactive and engaging.

| ![Meowbot Image 3](https://github.com/hlopushkaa/photomeowbot/blob/main/gh.jpg) | ![Meowbot Image 4](https://github.com/hlopushkaa/photomeowbot/blob/main/adf.jpg) |
| --- | --- |



# What's behind?
   
   The main software part is the skill for Yandex Station Alisa, which I wrote in the python programming language. Thanks to this skill, children can practice in a group setting. Alice asks questions in the voice of a cat, and the children answer. For example: what is the hottest time of the year? And if the children answer “summer,” then Alice will praise the children and ask the next question, and if the children answer incorrectly three times, then Alice will say the correct answer and explain why this particular answer is correct. During physical education warm-ups, Alice asks the children the song they want to warm up to. An equally important technical part is the code for interaction between Yandex Alice and the robot. Alice connects to the ESP32 board, which has a built-in wi-fi module, thanks to which the robot and Alice station interact. When the physical education warm-up begins, Alice transmits a signal to the board and the robot begins its movement (shows various physical exercises to children). The robot's movement is written in the Arduino IDE program. MeowBot has a large tablet on which children study individually. There is an educational game on the tablet that I wrote in Android Studio. All elements of the robot are interconnected, so the meowbot works clearly and without errors.

## The main technical parts of the robot

| Robot part | Purpose |
| --- | --- |
| Yandex Station Alisa Light | Interaction with children: communication, group activities, development of communication skills |
| ESP32 DevKit ESP-WROOM-32 V1 | Board with wi-fi module for interaction of Arduino with Yandex Station Alisa light |
| Arduino MG995 servo motor | Two servomotors for the movement of the robot, two servomotors for the movement of the meowbot’s paws (for physical education warm-ups) |
| Samsung Galaxy Tab S3 | Individual lessons in the form of educational games on a tablet |
| WS2812B IC RGB LED 16x16 | LED matrix for visualizing meowbot eyes |

