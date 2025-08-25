# Animal Shelter Dashboard & CRUD Module

This repository contains two main components:

1. **CRUD Python Module (`animal_shelter.py`)**  
   A Python class (`AnimalShelter`) that provides Create, Read, Update, and Delete (CRUD) functionality for the Austin Animal Center dataset stored in MongoDB.

2. **Dashboard (`ProjectTwoDashboard.ipynb`)**  
   A Jupyter Notebook dashboard built using Dash and Plotly, which connects to the CRUD module to provide interactive visualization and filtering of animal shelter data for the Grazioso Salvare organization.

---

## Reflection

### 1. Writing Maintainable, Readable, and Adaptable Programs
To ensure maintainability and readability, I separated database operations into a **dedicated CRUD module**. This modular design allowed me to reuse the `AnimalShelter` class in the dashboard project without rewriting database logic. Clear function names (`create`, `read`, `update`, `delete`) and error handling with exceptions improved adaptability.  

The advantage of this approach was that when I built the dashboard in Project Two, I could focus solely on visualization and user interaction, knowing the database interface was already stable and tested. In the future, this CRUD module could be adapted to other datasets or dashboards simply by pointing it to a different MongoDB collection.

---

### 2. My Approach as a Computer Scientist
When Grazioso Salvare requested database and dashboard functionality, I approached the problem systematically:
- **Step 1: Requirements Analysis** – Identify what the client needed (filtering by breed, visualizing outcomes, supporting rescue operations).  
- **Step 2: Modular Design** – Build the CRUD module first, then integrate it into the dashboard.  
- **Step 3: Testing and Iteration** – Test queries and visualizations, refine based on usability.

Compared to earlier coursework, this project was more client-focused and emphasized scalability and professional practices. In future database projects, I would continue using this modular and iterative approach, starting with reusable backend logic and layering client-specific features on top.

---

### 3. The Role of Computer Scientists
Computer scientists design solutions that turn raw data into actionable insights. In this project, my work helps Grazioso Salvare quickly identify dogs suitable for rescue training, saving time and improving outcomes.  

This matters because organizations depend on efficient data tools to make better decisions. By developing maintainable code and interactive dashboards, computer scientists empower companies to analyze data, optimize workflows, and ultimately achieve their mission more effectively.
