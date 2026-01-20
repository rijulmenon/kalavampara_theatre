# kalavampara_theatre
A Python and MySQL–based theatre seat booking system with a user-friendly GUI for real-time seat selection, pricing, and booking management along with an admin interface.


Kalavampura Theater is a Python-based desktop application that simulates a real-world movie theatre seat booking system. The project provides an interactive graphical interface where users can view seat availability, select seats visually, calculate ticket prices automatically, and confirm bookings with database support.

The application is built using Python (Tkinter) for the GUI and MySQL for backend data storage. Seats are displayed in a theatre-style layout with color coding—green for available seats, red for selected seats, and grey for already booked seats—making the booking process intuitive and user-friendly.

Once booking is completed, seat details and pricing information can be stored securely in the database, ensuring that previously booked seats remain unavailable for future users. The project demonstrates practical usage of GUI programming, database connectivity, event handling, and file management concepts.


  FOR A MORE DETAILED EXPLAINATION OF EACH FUNCTION AND FRAME - GO THROUGH THE PROJECT REPORT

## SOME EXTRACT FROM THE OVERVIEW GIVEN IN THE REPORT
## 1.The Welcome Screen:
The application opens with a friendly welcome screen, which acts as the initial point of interaction. It boasts an appealing design that showcases the app logo along with a concise introduction, ensuring a user-friendly experience and an easy-to-navigate program. It consists of a colourful box and spirals of different colours with the Theater’s name.
<img width="913" height="906" alt="image" src="https://github.com/user-attachments/assets/74e0c546-235f-4ea5-a303-d92dbe16639a" />

## 2.The Main Screen:
The main screen is the hub of the application, where users can either login as a customer or admin. The Admin login is in far top left while customer login in the top right corner. Customers can browse through a selection of currently available movies sorted in various languages.
<img width="918" height="771" alt="image" src="https://github.com/user-attachments/assets/db1c5ae1-0001-4d71-84d3-03e68f3c968a" />

## 3.Login Page:
The login page is your secure and user-friendly entry point, featuring fields for your username and password. It is linked to mysql table CUSTOMER. New users may also register.
<img width="467" height="518" alt="image" src="https://github.com/user-attachments/assets/209cb6fb-46cd-45c7-8f2d-06908546e8cd" />
<img width="353" height="299" alt="image" src="https://github.com/user-attachments/assets/bb2e5d2a-2e06-4cee-b609-f49c234a802a" />

## 4.The Movie List:
Each of the languages shown in the main screen have two movies. The movies are shown with their official posters. The customer may choose a movie as per their wish.
<img width="409" height="439" alt="image" src="https://github.com/user-attachments/assets/15321e93-ce8d-4577-aa26-d81f8092b15c" />

## 5.Movie Details:
Each movie is presented with its brief description, the genre of the movie, duration and cast of the film. A link is also attached, this link redirects the user to the official trailer of the movie. Then,
user may book their seats according to availability and likings.

<img width="338" height="285" alt="image" src="https://github.com/user-attachments/assets/8752556a-5f1f-4d5c-a809-4805c95e2209" />

## 6.Seat Booking:
To ensure a hassle-free experience, plan ahead by checking schedules early to secure your preferred seats. Consider your seating preferences here. The Grey seats are the seats already booked. This data is gathered from mysql table of that movie. A clear button is also present which allows to clear all selected seats and book button to continue with the booking.

<img width="336" height="402" alt="image" src="https://github.com/user-attachments/assets/a7cb2cb9-766e-4e05-97b2-78602379a13c" />

## 7.Snacks Booking:
To ensure a comfortable experience, pre-order the snacks for the show. With vide range of food items, and lots of supply. A slider is in-cooperated for easier and simpler booking.
<img width="315" height="430" alt="image" src="https://github.com/user-attachments/assets/c3f6f0c1-c34e-45d1-a22e-287756b78a82" />

## 8.Final Receipt:
The receipt shows the total money along with the discounts available. It shows a descriptive detail of the order made of seats booking along with snacks ordered. Once the order is confirmed, the details are stored in mysql.

<img width="394" height="433" alt="image" src="https://github.com/user-attachments/assets/4e94d238-018a-45f7-85a5-2bd3950bc2a9" />
<img width="395" height="207" alt="image" src="https://github.com/user-attachments/assets/a52e83a7-a265-4dd1-b9d7-d541ed0b1363" />

## 9.Admin Login:
From the Menu Screen, we can also login as Admin. First, it alerts the user that they will be trying to access admin. Only one certain set of Username and passcode can grant access.
<img width="353" height="206" alt="image" src="https://github.com/user-attachments/assets/822031bc-f2b3-495f-81d9-342cbfaf1a6e" />
<img width="270" height="307" alt="image" src="https://github.com/user-attachments/assets/c59bf628-267f-491d-a6ad-400705e32cb1" />

## 10.Admin Page:
All the six available movies are shown. Each movie then showcases all the customers who have booked that particular movie.

<img width="318" height="407" alt="image" src="https://github.com/user-attachments/assets/d61058f5-97fe-4d28-8b39-da1ddbac969b" />

## 11.Movie Admin:
This window shows all the users which have booked in that particular movie. This data is retrieved from the mysql table of that movie table. There is a search bar which can used for easily finding a user. Additionally, if a user is clicked: It shows the entire details of the user like username, password, account id and all the movies booked by that particular user.
<img width="726" height="403" alt="image" src="https://github.com/user-attachments/assets/7de22aeb-92ef-4467-ae12-7d9df70ea513" />
<img width="743" height="408" alt="image" src="https://github.com/user-attachments/assets/c2256080-5bca-4e1e-9c59-9b3b9aa8c880" />
<img width="301" height="337" alt="image" src="https://github.com/user-attachments/assets/b4c760a3-7e20-4462-a713-20ab0351d2a7" />
