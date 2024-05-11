import psycopg2
conn = psycopg2.connect(user='postgres',
                              password='rat',
                              host='localhost',
                              port=5432,
                              database='hospital')

# Create a cursor object to interact with the database
cur = conn.cursor()

# Function to add a patient
def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input('enter patient gender: ')
    phone_number = int(input("enter patient phone number: "))
    address = input("enter patient address: ")

    # Query to insert patient details into the patients table
    query = "INSERT INTO patients (name, age,gender,phone_number,address) VALUES (%s, %s,%s,%s,%s)"
    cur.execute(query, (name, age,gender,phone_number,address))
    conn.commit()
    print("Patient added successfully!")

# Function to view doctors
def view_doctors():
    # Query to select all doctors from the doctors table2
    query = "SELECT * FROM doctors"
    cur.execute(query)
    doctors = cur.fetchall()

    for doctor in doctors:
        print(f"Doctor ID: {doctor[0]}, Name: {doctor[1]}, Specialization: {doctor[2]}")

# Function to book an appointment
def book_appointment():
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")

    # Query to insert appointment details into the appointments table
    query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date) VALUES (%s, %s, %s)"
    cur.execute(query, (patient_id, doctor_id, appointment_date))
    conn.commit()
    print("Appointment booked successfully!")

# Function to check appointments for a patient
def check_appointments():
    patient_id = int(input("Enter patient ID: "))

    # Query to select appointments for the given patient
    query = "SELECT * FROM appointments WHERE patient_id = %s"
    cur.execute(query, (patient_id,))
    appointments = cur.fetchall()

    for appointment in appointments:
        print(f"Appointment ID: {appointment[0]}, Patient ID: {appointment[1]}, Doctor ID: {appointment[2]}, Date: {appointment[3]}")

# Main program loop
while True:
    print("\n==== Hospital Management System ====")
    print("1. Add Patient")
    print("2. View Doctors")
    print("3. Book Appointment")
    print("4. Check Appointments")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_doctors()
    elif choice == "3":
        book_appointment()
    elif choice == "4":
        check_appointments()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
cur.close()
conn.close()