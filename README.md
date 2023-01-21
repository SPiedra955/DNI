# What is DNI ? 

The electronic DNI, or DNIe, is the personal and non-transferable National Identity Document, assigned to each Spanish citizen by public administration. It allows its bearer to physically and electronically prove their identity, as well as digitally sign electronic documents with the same legal validity as a handwritten signature. It is designed to provide its users with greater security, speed and convenience in carrying out administrative and commercial procedures.

![image](https://user-images.githubusercontent.com/114516225/210286175-902366f9-9c81-4e13-966f-0f731e177b5f.png)

# kata DNI

Write a program that, given a DNI number, obtains the letter of the NIF. The letter corresponding to a DNI is calculated using the following algorithm:
The remainder is obtained by dividing the ID number by 23.The resulting number indicates the position of the letter corresponding to that DNI in the following string:

assignation table:

![image](https://user-images.githubusercontent.com/114516225/210286356-3d10479c-4c23-4112-9ee0-8d21356f0472.png)

The letters are not used: I, Ñ, O, U.
The "I" and "O" are avoided to avoid confusion with other characters, such as "1", "l" or "0".

Build the program using a vector to store each of the letters in the table above. It then uses a dictionary to store the mapping table. It divides the code by a logic layer and a data access layer so that changes in the data structure used (vector or dictionary) do not imply changes in the code corresponding to the logic.

# Domain Drive Design(DDD)

### What is Domain ?

The word Domain used in context of software development refers to business. In the process of application development, term domain logic or business logic is commonly used. Basically, business logic is area of knowledge around which application logic revolves. The business logic of an application is a set of rules and guidelines that explain how business object should interact with each other to process modeled data.

### Why DDD ?

* Effective communication between domain experts and technical experts through Ubiquitous Languge.
* Focus on the development of a split area of the domain (subdomain) through Bounded Context's.
* Software is closer to the domain, and therefore closer to the customer.
* Well organized code, allowing the testing of the different parts of the domain in isolation.
* Business logic resides in one place and divided by contexts.
  Long-term maintainability.
 
 ### DNI domain through UML diagram

![image](https://user-images.githubusercontent.com/114516225/213879235-6d9e1c8e-f0cc-4ee1-93e5-c89588ab132d.png)
