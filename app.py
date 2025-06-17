from dotenv import load_dotenv
import streamlit as st
from streamlit_extras import add_vertical_space as avs 
import google.generativeai as genai 
import os
from PIL import Image 

load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

input_prompt_template = """ 
You are an AI language model that can convert plain English descriptions of database queries into valid SQL statements. 
Your task is to read an English description of a query and output the corresponding SQL query.

Follow these guidelines:

Identify the table(s) involved.
Determine the specific columns needed.
Recognise any conditions or filters that should be applied.
Format the SQL properly.
Here are some examples:
 
Example 1:
Input: "Retrieve the names and ages of all employees who are older than 30 years."
Output: SELECT name, age FROM employees
        WHERE age>30;
Example 2: 
Input: "Get the total sales amount from the orders table."
Output: SELECT SUM(amount) FROM orders;

Example 3:
Input: "Find the list of customers who made purchases in the last month, sorted by the date of purchase in  descending order."
Output: SELECT customer_name FROM purchases
        WHERE purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
        ORDER BY purchase_date DESC;
Example 4:
Input: "Show the average salary of employees grouped by department. "
Output: SELECT department, AVG(salary) FROM employees
        GROUP BY department;
Your task: Convert the following English descriptions into SQL queries.
Input: {sql_text}

Things you need to remember everytime-
Print - "SQL Query: " and from the next line write the sql query snippet 
Present the results following the same format as the examples provided above.
Breal the query snippet as shown in examples
"""
#Streamlit UI configuration 
st.set_page_config(page_title = "Text to SQL Query", layout = "wide")
avs.add_vertical_space(4)
col1, col2 = st.columns([3,2])
with col1:
    st.title("QueryCraft")
    st.header("Making Database Queries as Easy as Conversation!")
    st.markdown(
        """<p stryle ='text-align: justify;'>
        Introducing QueryCraft, your revolutionary solution for simplifying database interactions through natural language queries. Powered by a cutting-edge Large Language Model(LLM), 
        QueryCraft seamlessly converts everyday language into accurate SQL queries, eliminating the need for SQL experstise. Whether you're a business analyst seeking quick insights, a customer support representative streamlining data retrieval, or an educator enhancing student learning experiences, QueryCraft offers versatile solutions tailored to your needs. Say goodbye to complex database interacions and hello to effortless data access with QueryCraft. Unlock the power of natural language querying today!
        </p>""", unsafe_allow_html = True 
    
    )
with col2:
    img = Image.open("images/icon.png")
    st.image(img, use_column_width = True)
col1, col2 = st.columns([3,2])
with col2: 
    st.header("Wide Range of Offerings")
    st.write(" - Seamless Natural Language to SQL Conversion: Effortlessly convert natural language questions into SQL queries.")
    st.write(" - Business Analytics: Enable business analysts to quickly access and analyse data without needing SQL expertise.")
    st.write(" - Customer Support: Streamline data retrieval for customer support representatives, reducing response times amd enhancing customer satisfaction.")
    st.write(" - Educational Tools: Assist students in learning SQL by allowing them to input queries in simple English. ")
    st.write(" - Increased Productivity: Improve decision-making and productivity by simplifying database interactions. ")
    st.write(" - Intuitive User Experience: Provide an intuitive and engaging experience for users across various scenarios. ")
    st.write(" - Versatile Solutions: Cater to the needs of business analytics, customer support representatives, and educators.")

with col1:
    img1 = Image.open("images/icon1.png")
    st.image(img1, use_column_width  = True)
col1, col2 = st.columns([3,2])
with col1:
    st.markdown("<h1 style  = 'text-align: centre;'>Start Your Query Conversation</h1>", unsafe_allow_html = True)
    sql_text = st.text_area("Provide the text")

    submit = st.button("Submit")
    if submit: 
        imput_prompt = input_prompt_template.format(sql_text = sql_text)
        response = get_gemini_response(input_prompt)
        st.subheader(response)

with col2:
    img2 = Image.open("images/icon2.png")
    st.image(img2, use_column_width = True)

col1, col2 = st.columns([2,3])
with col2:
    st.write("Question: What is QueryCraft?")
    st.write(""" Answer: QueryCraft is an advanced project powered by a Large Language Model (LLM) that converts natural langugae questions into SQL gueries, simplifying database interactions for users without SQL expertise. """)
    avs.add_vertical_space(3)
    st.write("Question: How can QueryCraft help business analysts?")
    st.write("""Answer: QueryCraft allows business analysts to ask questions in natural language and these questions into accurate SQL queries. This enables analysts to quickly access and analyse improving productivity and decision-making.""" )
    
    avs.add_vertical_space(3)
    st.write("Question: Can QueryCraft be used in customer support?")
    st.write(""" Answer: Yes, customer support representatives can use QueryCraft to input questions like 'Show the recent ordrrs placed by user ID 12345,' which the LLM converts into SQL queries. This helps in quick and efficient data retrieval, reducing response times and enhancing customer satisfaction.""" )
with col1:
    avs.add_vertical_space(8)
    img3 = Image.open("images/icon3.png")
    st.image(img3, use_column_width = True)