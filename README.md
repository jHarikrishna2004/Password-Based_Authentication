Password Strength Checker Project
-------------------------------------------------------------------
Description

This repository contains the source code for a Flask-based Password Strength Checker Web Application. The project validates user passwords based on security rules and provides feedback such as Weak, Medium, or Strong. If the password is strong, the user is granted access to a protected “About” page.

The application is built using a modular backend structure in Python with Flask and a simple HTML frontend using templates.

___________________________________________________________________
Project Structure

passwordcheck/
│── app.py                 
│── main.py              
│── password_logic.py 
│── requirements.txt  
│── README.md           
│
├── templates/        
│     ├── index.html     
│     └── about.html 

___________________________________________________________________
Features
- User password input system
- Password strength validation (Weak / Medium / Strong)
- Secure access control to protected page
- Backend logic using Flask (Python)
- Simple and clean UI using HTML templates
- Modular and scalable project structure

___________________________________________________________________
Technologies Used
- Backend: Flask (Python)
- Frontend: HTML
- Logic: Python (password validation module)

___________________________________________________________________
Installation
1. Clone the repository
   git clone https://github.com/jHarikrishna2004/Password-Based_Authentication.git
   
   cd passwordcheck
   
3. Install backend dependencies
   pip install -r requirements.txt
   
5. Run the backend server
   python app.py

___________________________________________________________________
Usage
Open browser and go to:
   http://127.0.0.1:5000
Enter a password
System checks strength:
  Weak → shows suggestions
  Medium → suggests improvements
  Strong → redirects to About page

  ___________________________________________________________________
Contributing
- Fork the repository
- Create a feature branch
- Commit changes
- Push to branch
- Open a Pull Request
___________________________________________________________________
License
This project is open-source and free to use.
