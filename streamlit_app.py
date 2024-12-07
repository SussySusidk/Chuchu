import streamlit as st

# Title of the Streamlit app
st.title("Program 1: Temperature")

# C program code as a string
c_program_code = """
#include <stdio.h>
#define DAYS 30 // Constant for the number of days in a month

// Function declarations
void inputTemperatures(float temps[]);
float calculateAverage(float temps[]);
void findMaxMinTemps(float temps[], float *max, float *min, int *maxDay, int *minDay);
int countAboveAverage(float temps[], float average);

int main() {
    float temperatures[DAYS];
    float averageTemp, maxTemp, minTemp;
    int maxDay, minDay, aboveAverageCount;

    // Input temperatures for 30 days
    inputTemperatures(temperatures);

    // Calculate average temperature
    averageTemp = calculateAverage(temperatures);
    printf("\\nAverage Temperature: %.2f°C\\n", averageTemp);

    findMaxMinTemps(temperatures, &maxTemp, &minTemp, &maxDay, &minDay);
    printf("Maximum Temperature: %.2f°C on Day %d\\n", maxTemp, maxDay + 1);
    printf("Minimum Temperature: %.2f°C on Day %d\\n", minTemp, minDay + 1);

    // Count days above average temperature
    aboveAverageCount = countAboveAverage(temperatures, averageTemp);
    printf("Number of days with temperature above average: %d\\n", aboveAverageCount);

    return 0;
}

void inputTemperatures(float temps[]) {
    for (int i = 0; i < DAYS; i++) {
        printf("Enter temperature for Day %d: ", i + 1);
        scanf("%f", &temps[i]);
    }
}

// Function to calculate average temperature
float calculateAverage(float temps[]) {
    float sum = 0;
    for (int i = 0; i < DAYS; i++) {
        sum += temps[i];
    }
    return sum / DAYS;
}

// Function to find the maximum and minimum temperatures and their respective days
void findMaxMinTemps(float temps[], float *max, float *min, int *maxDay, int *minDay) {
    *max = temps[0];
    *min = temps[0];
    *maxDay = 0;
    *minDay = 0;

    for (int i = 1; i < DAYS; i++) {
        if (temps[i] > *max) {
            *max = temps[i];
            *maxDay = i;
        }
        if (temps[i] < *min) {
            *min = temps[i];
            *minDay = i;
        }
    }
}

// Function to count how many days had a temperature above the average
int countAboveAverage(float temps[], float average) {
    int count = 0;
    for (int i = 0; i < DAYS; i++) {
        if (temps[i] > average) {
            count++;
        }
    }
    return count;
}
"""

# Display the C program code using Streamlit markdown
st.markdown(f"```c\n{c_program_code}\n```")

# Title of the Streamlit app
st.title("Program 2: Library Management System")

# C program code as a string
library_management_code = """
#include <stdio.h>
#include <string.h>

#define MAX_BOOKS 100
#define MAX_TITLE_LENGTH 100

// Function declarations
void addBook(char books[][MAX_TITLE_LENGTH], int *count);
void searchBook(char books[][MAX_TITLE_LENGTH], int count);
void displayBooks(char books[][MAX_TITLE_LENGTH], int count);
void removeBook(char books[][MAX_TITLE_LENGTH], int *count);

int main() {
    char books[MAX_BOOKS][MAX_TITLE_LENGTH]; // Array to store up to 100 book titles
    int bookCount = 0; // Number of books currently in the library
    int choice;
    do {
        // Display menu options
        printf("\\nLibrary Management System:\\n");
        printf("1. Add a Book\\n");
        printf("2. Search for a Book\\n");
        printf("3. Display All Books\\n");
        printf("4. Remove a Book\\n");
        printf("5. Exit\\n");
        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);
        getchar(); // To consume the newline character after scanf
        switch (choice) {
            case 1:
                addBook(books, &bookCount);
                break;
            case 2:
                searchBook(books, bookCount);
                break;
            case 3:
                displayBooks(books, bookCount);
                break;
            case 4:
                removeBook(books, &bookCount);
                break;
            case 5:
                printf("Exiting the program.\\n");
                break;
            default:
                printf("Invalid choice. Please select a valid option.\\n");
        }
    } while (choice != 5);
    return 0;
}

// Function to add a book to the library
void addBook(char books[][MAX_TITLE_LENGTH], int *count) {
    if (*count < MAX_BOOKS) {
        printf("Enter the title of the book: ");
        fgets(books[*count], MAX_TITLE_LENGTH, stdin);
        books[*count][strcspn(books[*count], "\\n")] = 0; // Remove newline character
        (*count)++;
        printf("Book added successfully.\\n");
    } else {
        printf("Library is full. Cannot add more books.\\n");
    }
}

// Function to search for a book in the library
void searchBook(char books[][MAX_TITLE_LENGTH], int count) {
    char title[MAX_TITLE_LENGTH];
    int found = 0;
    printf("Enter the title of the book to search: ");
    fgets(title, MAX_TITLE_LENGTH, stdin);
    title[strcspn(title, "\\n")] = 0; // Remove newline character
    for (int i = 0; i < count; i++) {
        if (strcmp(books[i], title) == 0) {
            printf("The book \"%s\" is available in the library.\\n", title);
            found = 1;
            break;
        }
    }
    if (!found) {
        printf("The book \"%s\" is not available in the library.\\n", title);
    }
}

// Function to display all books in the library
void displayBooks(char books[][MAX_TITLE_LENGTH], int count) {
    if (count == 0) {
        printf("No books in the library.\\n");
    } else {
        printf("Books currently in the library:\\n");
        for (int i = 0; i < count; i++) {
            printf("%d. %s\\n", i + 1, books[i]);
        }
    }
}

// Function to remove a book from the library
void removeBook(char books[][MAX_TITLE_LENGTH], int *count) {
    char title[MAX_TITLE_LENGTH];
    int found = 0;

    if (*count == 0) {
        printf("No books to remove.\\n");
        return;
    }
    printf("Enter the title of the book to remove: ");
    fgets(title, MAX_TITLE_LENGTH, stdin);
    title[strcspn(title, "\\n")] = 0; // Remove newline character

    for (int i = 0; i < *count; i++) {
        if (strcmp(books[i], title) == 0) {
            // Shift all subsequent books one position to the left
            for (int j = i; j < *count - 1; j++) {
                strcpy(books[j], books[j + 1]);
            }
            (*count)--;
            printf("The book \"%s\" has been removed from the library.\\n", title);
            found = 1;
            break;
        }
    }
    if (!found) {
        printf("The book \"%s\" was not found in the library.\\n", title);
    }
    // Display updated list of books
    displayBooks(books, *count);
}
"""

# Display the C program code using Streamlit markdown
st.markdown(f"```c\n{library_management_code}\n```")


st.title("Program 3: Web forward/backward using stack")
# C program code as a string
browser_navigation_code = """
#include <stdio.h>
#include <string.h>

#define MAX_HISTORY 100
#define MAX_URL_LENGTH 100

// Stack structure for storing URLs
typedef struct {
    char urls[MAX_HISTORY][MAX_URL_LENGTH];
    int top;
} Stack;

// Function declarations
void push(Stack *stack, char *url);
char *pop(Stack *stack);
int isEmpty(Stack *stack);
void visitNewWebsite(Stack *backStack, Stack *forwardStack, char *currentWebsite);
void goBack(Stack *backStack, Stack *forwardStack, char *currentWebsite);
void goForward(Stack *backStack, Stack *forwardStack, char *currentWebsite);
void displayCurrentWebsite(char *currentWebsite);

int main() {
    Stack backStack = {.top = -1}; // Stack to store "Back" history
    Stack forwardStack = {.top = -1}; // Stack to store "Forward" history
    char currentWebsite[MAX_URL_LENGTH] = "home"; // Starting page (home)
    int choice;

    do {
        // Display menu options
        printf("\\nBrowser Navigation System:\\n");
        printf("1. Visit a New Website\\n");
        printf("2. Go Back to Previous Website\\n");
        printf("3. Go Forward to Next Website\\n");
        printf("4. Display Current Website\\n");
        printf("5. Exit\\n");
        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);
        getchar(); // To consume newline character after scanf

        switch (choice) {
            case 1: {
                char newWebsite[MAX_URL_LENGTH];
                printf("Enter the URL of the new website: ");
                fgets(newWebsite, MAX_URL_LENGTH, stdin);
                newWebsite[strcspn(newWebsite, "\\n")] = 0; // Remove newline
                visitNewWebsite(&backStack, &forwardStack, currentWebsite);
                strcpy(currentWebsite, newWebsite);
                break;
            }
            case 2:
                goBack(&backStack, &forwardStack, currentWebsite);
                break;
            case 3:
                goForward(&backStack, &forwardStack, currentWebsite);
                break;
            case 4:
                displayCurrentWebsite(currentWebsite);
                break;
            case 5:
                printf("Exiting the program.\\n");
                break;
            default:
                printf("Invalid choice. Please select a valid option.\\n");
        }
    } while (choice != 5);
    return 0;
}

// Function to push a URL onto a stack
void push(Stack *stack, char *url) {
    if (stack->top < MAX_HISTORY - 1) {
        stack->top++;
        strcpy(stack->urls[stack->top], url);
    } else {
        printf("Stack is full. Cannot push more URLs.\\n");
    }
}

// Function to pop a URL from a stack
char *pop(Stack *stack) {
    if (!isEmpty(stack)) {
        return stack->urls[stack->top--];
    } else {
        return NULL;
    }
}

// Function to check if a stack is empty
int isEmpty(Stack *stack) {
    return stack->top == -1;
}

// Function to visit a new website
void visitNewWebsite(Stack *backStack, Stack *forwardStack, char *currentWebsite) {
    // Push the current website onto the back stack
    push(backStack, currentWebsite);
    // Clear the forward stack
    forwardStack->top = -1;
    printf("Visited a new website.\\n");
}

// Function to go back to the previous website
void goBack(Stack *backStack, Stack *forwardStack, char *currentWebsite) {
    if (!isEmpty(backStack)) {
        // Push the current website onto the forward stack
        push(forwardStack, currentWebsite);
        // Pop the previous website from the back stack and update currentWebsite
        strcpy(currentWebsite, pop(backStack));
        printf("Went back to: %s\\n", currentWebsite);
    } else {
        printf("No more history to go back.\\n");
    }
}

// Function to go forward to the next website
void goForward(Stack *backStack, Stack *forwardStack, char *currentWebsite) {
    if (!isEmpty(forwardStack)) {
        // Push the current website onto the back stack
        push(backStack, currentWebsite);
        // Pop the next website from the forward stack and update currentWebsite
        strcpy(currentWebsite, pop(forwardStack));
        printf("Went forward to: %s\\n", currentWebsite);
    } else {
        printf("No more forward history.\\n");
    }
}

// Function to display the current website
void displayCurrentWebsite(char *currentWebsite) {
    printf("Current website: %s\\n", currentWebsite);
}
"""

# Display the C program code using Streamlit markdown
st.markdown(f"```c\n{browser_navigation_code}\n```")

st.title("Program 4: Evaluation of Suffix Expression and Tower of Hanoi")

# Part A: Evaluation of Suffix Expression
suffix_expression_code = """
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int i, top = -1;
int op1, op2, res, s[20];
char postfix[90], symb;

void push(int item) {
    top = top + 1;
    s[top] = item;
}

int pop() {
    int item;
    item = s[top];
    top = top - 1;
    return item;
}

void main() {
    printf("\\nEnter a valid postfix expression:\\n");
    scanf("%s", postfix);

    for(i = 0; postfix[i] != '\\0'; i++) {
        symb = postfix[i];

        if(isdigit(symb)) {
            push(symb - '0');
        } else {
            op2 = pop();
            op1 = pop();
            switch(symb) {
                case '+': push(op1 + op2); break;
                case '-': push(op1 - op2); break;
                case '*': push(op1 * op2); break;
                case '/': push(op1 / op2); break;
                case '%': push(op1 % op2); break;
                case '^': push(pow(op1, op2)); break;
                default: push(0); break;
            }
        }
    }

    res = pop();
    printf("\\nResult = %d", res);
}
"""

# Part B: Tower of Hanoi
tower_of_hanoi_code = """
#include <stdio.h>

// C recursive function to solve Tower of Hanoi puzzle
void towerOfHanoi(int n, char from_rod, char to_rod, char aux_rod) {
    if (n == 1) {
        printf("\\nMove disk 1 from rod %c to rod %c", from_rod, to_rod);
        return;
    }

    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod);
    printf("\\nMove disk %d from rod %c to rod %c", n, from_rod, to_rod);
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod);
}

int main() {
    int n = 4; // Number of disks
    towerOfHanoi(n, 'A', 'C', 'B'); // A, B, and C are names of rods
    return 0;
}
"""

# Display Part A code
st.subheader("Part A: Evaluation of Suffix Expression")
st.markdown(f"```c\n{suffix_expression_code}\n```")

# Display Part B code
st.subheader("Part B: Solving Tower of Hanoi")
st.markdown(f"```c\n{tower_of_hanoi_code}\n```")


st.title("Program 5: Hospital Patient Management System")

# Hospital Patient Management System Code
patient_management_code = """
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the structure for a Patient
struct Patient {
    int id;
    char name[50];
    int age;
    struct Patient* next;
};

// Initialize head pointer to NULL
struct Patient* head = NULL;

// Function to add a new patient at the end of the list
void addPatient(int id, char name[], int age) {
    struct Patient* newPatient = (struct Patient*)malloc(sizeof(struct Patient));
    newPatient->id = id;
    strcpy(newPatient->name, name);
    newPatient->age = age;
    newPatient->next = NULL;
    if (head == NULL) {
        head = newPatient; // If list is empty, new patient becomes the head
    } else {
        struct Patient* temp = head;
        while (temp->next != NULL) {
            temp = temp->next; // Traverse to the last node
        }
        temp->next = newPatient; // Link the new patient at the end
    }
}

// Function to display all patients in the list
void displayPatients() {
    struct Patient* temp = head;
    if (temp == NULL) {
        printf("No patients in the list.\\n");
        return;
    }
    printf("Patient List:\\n");
    while (temp != NULL) {
        printf("ID: %d, Name: %s, Age: %d\\n", temp->id, temp->name, temp->age);
        temp = temp->next;
    }
}

// Function to search for a patient by ID
void searchPatient(int id) {
    struct Patient* temp = head;
    while (temp != NULL) {
        if (temp->id == id) {
            printf("Patient found - ID: %d, Name: %s, Age: %d\\n", temp->id, temp->name, temp->age);
            return;
        }
        temp = temp->next;
    }
    printf("Patient with ID %d not found.\\n", id);
}

// Function to delete a patient by ID
void deletePatient(int id) {
    struct Patient* temp = head;
    struct Patient* prev = NULL;
    if (temp != NULL && temp->id == id) {
        head = temp->next; // Patient to be deleted is the head
        free(temp);
        printf("Patient with ID %d deleted.\\n", id);
        return;
    }
    while (temp != NULL && temp->id != id) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) {
        printf("Patient with ID %d not found.\\n", id);
        return;
    }
    prev->next = temp->next; // Unlink the patient from the list
    free(temp);
    printf("Patient with ID %d deleted.\\n", id);
}

// Function to count the total number of patients
void countPatients() {
    struct Patient* temp = head;
    int count = 0;
    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    printf("Total number of patients: %d\\n", count);
}

int main() {
    int choice, id, age;
    char name[50];

    while (1) {
        printf("\\nHospital Patient Management System\\n");
        printf("1. Add New Patient\\n");
        printf("2. Display All Patients\\n");
        printf("3. Search for Patient by ID\\n");
        printf("4. Delete Patient Record\\n");
        printf("5. Count Total Patients\\n");
        printf("6. Exit\\n");
        printf("Enter your choice: ");
        
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                printf("Enter Patient ID: ");
                scanf("%d", &id);
                printf("Enter Patient Name: ");
                scanf("%s", name);
                printf("Enter Patient Age: ");
                scanf("%d", &age);
                addPatient(id, name, age);
                break;
            case 2:
                displayPatients();
                break;
            case 3:
                printf("Enter Patient ID to search: ");
                scanf("%d", &id);
                searchPatient(id);
                break;
            case 4:
                printf("Enter Patient ID to delete: ");
                scanf("%d", &id);
                deletePatient(id);
                break;
            case 5:
                countPatients();
                break;
            case 6:
                printf("Exiting the program.\\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\\n");
        }
    }
    return 0;
}
"""

# Display the C program code using Streamlit markdown
st.subheader("Hospital Patient Management System Code")
st.markdown(f"```c\n{patient_management_code}\n```")

st.title("Program 7: Binary Tree: Level Order Traversal")

# Binary Tree Level Order Traversal Code
binary_tree_code = """
#include <stdio.h>
#include <stdlib.h>

// Structure of a tree node
struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
};

// Function to create a new tree node
struct TreeNode* createNode(int data) {
    struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to insert nodes into the binary tree level by level
struct TreeNode* insertLevelOrder(int arr[], struct TreeNode* root, int i, int n) {
    // Base case for recursion
    if (i < n) {
        struct TreeNode* temp = createNode(arr[i]);
        root = temp;
        // Insert left child
        root->left = insertLevelOrder(arr, root->left, 2 * i + 1, n);
        // Insert right child
        root->right = insertLevelOrder(arr, root->right, 2 * i + 2, n);
    }
    return root;
}

// Function to print the tree in level order (using in-order traversal for testing purposes)
void inOrderTraversal(struct TreeNode* root) {
    if (root != NULL) {
        inOrderTraversal(root->left);
        printf("%d ", root->data);
        inOrderTraversal(root->right);
    }
}

// Function to perform level-order traversal of the tree using a queue
void printLevelOrder(struct TreeNode* root) {
    if (root == NULL) return;
    // Create a queue
    struct TreeNode** queue = (struct TreeNode**)malloc(100 * sizeof(struct TreeNode*));
    int front = 0, rear = 0;
    // Enqueue root
    queue[rear++] = root;
    while (front < rear) {
        struct TreeNode* node = queue[front++];
        // Print current node
        printf("%d ", node->data);
        // Enqueue left child
        if (node->left != NULL)
            queue[rear++] = node->left;
        // Enqueue right child
        if (node->right != NULL)
            queue[rear++] = node->right;
    }
    free(queue);
}

int main() {
    // Example input array
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    // Create the binary tree from the array
    struct TreeNode* root = insertLevelOrder(arr, root, 0, n);
    // Print the tree in level order to verify the structure
    printf("Level order traversal of the constructed binary tree: \n");
    printLevelOrder(root);
    return 0;
}
"""

# Display the C program code using Streamlit markdown
st.subheader("Binary Tree: Level Order Traversal Code")
st.markdown(f"```c\n{binary_tree_code}\n```")

import streamlit as st

st.title("Program 8: Student Record Management System: Binary Search Tree (BST)")

# Student Record Management BST Code
student_record_code = """
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to represent a student record
struct Student {
    int rollNo;
    char name[100];
    float gpa;
    struct Student* left;
    struct Student* right;
};

// Function to create a new student node
struct Student* createStudent(int rollNo, char name[], float gpa) {
    struct Student* newStudent = (struct Student*)malloc(sizeof(struct Student));
    newStudent->rollNo = rollNo;
    strcpy(newStudent->name, name);
    newStudent->gpa = gpa;
    newStudent->left = NULL;
    newStudent->right = NULL;
    return newStudent;
}

// Insert a student record into the BST
struct Student* insertStudent(struct Student* root, int rollNo, char name[], float gpa) {
    // If the tree is empty, create a new student node and return it
    if (root == NULL) {
        return createStudent(rollNo, name, gpa);
    }
    // If the roll number is smaller, insert in the left subtree
    if (rollNo < root->rollNo) {
        root->left = insertStudent(root->left, rollNo, name, gpa);
    }
    // If the roll number is greater, insert in the right subtree
    else if (rollNo > root->rollNo) {
        root->right = insertStudent(root->right, rollNo, name, gpa);
    }
    // If the roll number already exists, do nothing (unique roll number required)
    else {
        printf("Student with roll number %d already exists!\\n", rollNo);
    }
    return root;
}

// Function to search for a student by roll number
struct Student* searchStudent(struct Student* root, int rollNo) {
    // Base case: root is null or rollNo is present at root
    if (root == NULL || root->rollNo == rollNo) {
        return root;
    }
    // Roll number is greater, search in the right subtree
    if (rollNo > root->rollNo) {
        return searchStudent(root->right, rollNo);
    }
    // Roll number is smaller, search in the left subtree
    return searchStudent(root->left, rollNo);
}

// Function to perform in-order traversal (display students in ascending order of rollNo)
void inOrderTraversal(struct Student* root) {
    if (root != NULL) {
        inOrderTraversal(root->left);
        printf("Roll No: %d, Name: %s, GPA: %.2f\\n", root->rollNo, root->name, root->gpa);
        inOrderTraversal(root->right);
    }
}

// Function to find the minimum value node in a BST
struct Student* findMinValueNode(struct Student* node) {
    struct Student* current = node;
    // Loop down to find the leftmost leaf (minimum value)
    while (current && current->left != NULL) {
        current = current->left;
    }
    return current;
}

// Function to delete a student by roll number
struct Student* deleteStudent(struct Student* root, int rollNo) {
    if (root == NULL) return root;
    // If the rollNo to be deleted is smaller, go to the left subtree
    if (rollNo < root->rollNo) {
        root->left = deleteStudent(root->left, rollNo);
    }
    // If the rollNo to be deleted is greater, go to the right subtree
    else if (rollNo > root->rollNo) {
        root->right = deleteStudent(root->right, rollNo);
    }
    // If rollNo matches, this is the node to be deleted
    else {
        // Node with only one child or no child
        if (root->left == NULL) {
            struct Student* temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL) {
            struct Student* temp = root->left;
            free(root);
            return temp;
        }
        // Node with two children: get the inorder successor (smallest in the right subtree)
        struct Student* temp = findMinValueNode(root->right);
        // Copy the inorder successor's content to this node
        root->rollNo = temp->rollNo;
        strcpy(root->name, temp->name);
        root->gpa = temp->gpa;
        // Delete the inorder successor
        root->right = deleteStudent(root->right, temp->rollNo);
    }
    return root;
}

// Function to display students with GPA above a certain threshold
void displayStudentsAboveGPA(struct Student* root, float threshold) {
    if (root != NULL) {
        displayStudentsAboveGPA(root->left, threshold);
        if (root->gpa > threshold) {
            printf("Roll No: %d, Name: %s, GPA: %.2f\\n", root->rollNo, root->name, root->gpa);
        }
        displayStudentsAboveGPA(root->right, threshold);
    }
}

int main() {
    struct Student* root = NULL;
    int choice, rollNo;
    char name[100];
    float gpa, threshold;
    while (1) {
        printf("\\nStudent Record Management System\\n");
        printf("1. Insert Student Record\\n");
        printf("2. Search Student Record\\n");
        printf("3. Delete Student Record\\n");
        printf("4. Display All Student Records (In-order Traversal)\\n");
        printf("5. Display Students with GPA Above Threshold\\n");
        printf("6. Exit\\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
        case 1:
            printf("Enter Roll No: ");
            scanf("%d", &rollNo);
            printf("Enter Name: ");
            scanf("%s", name);
            printf("Enter GPA: ");
            scanf("%f", &gpa);
            root = insertStudent(root, rollNo, name, gpa);
            break;
        case 2:
            printf("Enter Roll No to Search: ");
            scanf("%d", &rollNo);
            struct Student* student = searchStudent(root, rollNo);
            if (student != NULL) {
                printf("Student Found - Roll No: %d, Name: %s, GPA: %.2f\\n", student->rollNo, student->name, student->gpa);
            } else {
                printf("Student with Roll No %d not found!\\n", rollNo);
            }
            break;
        case 3:
            printf("Enter Roll No to Delete: ");
            scanf("%d", &rollNo);
            root = deleteStudent(root, rollNo);
            break;
        case 4:
            printf("Displaying All Student Records (In-order Traversal):\\n");
            inOrderTraversal(root);
            break;
        case 5:
            printf("Enter GPA Threshold: ");
            scanf("%f", &threshold);
            printf("Students with GPA above %.2f:\\n", threshold);
            displayStudentsAboveGPA(root, threshold);
            break;
        case 6:
            exit(0);
        default:
            printf("Invalid Choice! Please try again.\\n");
        }
    }
    return 0;
}
"""

# Display the C program code using Streamlit markdown
st.subheader("Student Record Management System: Binary Search Tree (BST) Code")
st.markdown(f"```c\n{student_record_code}\n```")

st.title("Program 10: Hash Table with Linear Probing")

# Hash Table Code
hash_table_code = """
#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10 // Size of the hash table

// Function to implement the hash function
int hashFunction(int key) {
    return key % TABLE_SIZE;
}

// Function to insert a key into the hash table using linear probing
void insert(int hashTable[], int key) {
    int index = hashFunction(key);
    // Linear probing in case of collision
    while (hashTable[index] != -1) {
        index = (index + 1) % TABLE_SIZE; // Move to the next index
    }
    hashTable[index] = key; // Insert the key at the found position
}

// Function to display the hash table
void display(int hashTable[]) {
    printf("Hash Table:\\n");
    for (int i = 0; i < TABLE_SIZE; i++) {
        if (hashTable[i] != -1)
            printf("Index %d: %d\\n", i, hashTable[i]);
        else
            printf("Index %d: Empty\\n", i);
    }
}

int main() {
    int hashTable[TABLE_SIZE];
    // Initialize the hash table to -1 (indicating empty slots)
    for (int i = 0; i < TABLE_SIZE; i++) {
        hashTable[i] = -1;
    }
    int numKeys;
    // Ask the user for the number of keys they want to insert
    printf("Enter the number of keys to insert: ");
    scanf("%d", &numKeys);
    
    // Dynamically create an array to store user input
    int keys[numKeys];
    // Get the keys from the user
    printf("Enter the keys:\\n");
    for (int i = 0; i < numKeys; i++) {
        printf("Key %d: ", i + 1);
        scanf("%d", &keys[i]);
    }
    
    // Insert the keys into the hash table
    for (int i = 0; i < numKeys; i++) {
        insert(hashTable, keys[i]);
    }
    
    // Display the hash table
    display(hashTable);
    
    return 0;
}
"""

# Display the C program code using Streamlit markdown
st.subheader("Hash Table with Linear Probing Code")
st.markdown(f"```c\n{hash_table_code}\n```")
