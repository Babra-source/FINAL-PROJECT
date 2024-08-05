from matplotlib import pyplot as plt
import streamlit as st
import pickle
import shap
import pandas as pd
import base64

# Load the model
filename = "Model_trained.sav"
model = pickle.load(open(filename, 'rb'))

# Initialize SHAP explainer
explainer = shap.Explainer(model)

# Function to get base64 of an image
def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Background image
background_image_base64 = get_base64_of_image("C:/Users/user/OneDrive - Ashesi University/Desktop/Final Ai project/student_gpa.jpeg")

# Markdown for the header and styling
st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">',
    unsafe_allow_html=True,
)
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)

hide_streamlit_style = """
    <style>
        header{visibility:hidden;}
        .main {
            margin-top: -20px;
            padding-top:10px;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

navbar_style = f"""
    <style>
        .navbar {{
            background: url(data:image/jpeg;base64,{background_image_base64}) no-repeat center center;
            background-size: cover;
        }}
    </style>
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark">
        <a class="navbar-brand" href="#" target="_blank">Grade Predict</a>  
    </nav>
"""
st.markdown(navbar_style, unsafe_allow_html=True)

def display_home_page():
    """Display the home page with a background image."""
    # Path to your background image
    background_image_path = "C:/Users/user/OneDrive - Ashesi University/Desktop/Final Ai project/Homepage.jpg"
    
    # Convert the image to Base64
    background_image_base64 = get_base64_of_image(background_image_path)
    
    # HTML and CSS for the background and content
    st.markdown(f"""
    <style>
    body {{
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: white;
    }}
    .home-container {{
        position: relative;
        font-family: Arial, sans-serif;
        line-height: 1.6;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background for readability */
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: auto;
        width: 80%;
        max-width: 1200px;
        margin-top: 100px; /* Adjust margin to center content */
    }}
    .home-title {{
        font-size: 3em;
        color: #333;
        text-align: center;
    }}
    .home-intro {{
        font-size: 1.2em;
        color: #555;
        text-align: center;
        margin-top: 20px;
    }}
    .cta-button {{
        display: inline-block;
        font-size: 1.2em;
        padding: 10px 20px;
        color: #fff;
        background-color: #007BFF;
        border: none;
        border-radius: 5px;
        text-decoration: none;
        text-align: center;
        margin-top: 20px;
    }}
    .cta-button:hover {{
        background-color: #0056b3;
    }}
    </style>
    <div class="home-container">
        <h1 class="home-title">Welcome to the GPA Prediction Platform</h1>
        <p class="home-intro">
            Discover how our advanced model can help you understand and predict your academic performance. 
            Whether you're looking to boost your grades or maintain your high performance, we're here to assist you in your academic journey with personalized insights and tips.
        </p>
    </div>
    """, unsafe_allow_html=True)

def process():
    st.title("Fill in the factors with your details:")

    # Create two columns for input fields
    col1, col2 = st.columns(2)

    with col1:
        # Input fields for user to enter data
        studytime = st.number_input('Study Time (hours per week)', min_value=0, max_value=10)
        reason = st.selectbox(
            'Reason for Choosing School', 
            options=[0, 1, 2, 3], 
            format_func=lambda x: {
                0: 'Course preference',
                1: 'Close to Home',
                2: 'Other',
                3: 'Reputation'
            }[x])
        
        higher = st.selectbox(
            'Want to take higher Education',
            options=[0, 1],
            format_func=lambda x: {
                1: 'Yes',
                0: 'No',
            }[x]
            )


          # Assuming encoded values
        traveltime = st.number_input('Travel Time (1-4)', min_value=1, max_value=4)
        Fedu = st.selectbox(
            'Father\'s Education Level',
            options=[1, 2, 3, 4],
            format_func=lambda x: {
                1: 'No formal education',
                2: 'Primary education',
                3: 'Completed primary education',
                4: 'Secondary education or higher',
            }[x])
        
        Dalc = st.selectbox(
            'Workday Alcohol Consumption',
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: 'Very Low',
                2: 'Low',
                3: 'Medium',
                4: 'High',
                5: 'Very High',
            }[x]
        )

    
    with col2:
        age = st.number_input('Age', min_value=0, max_value=100)
        failures = st.number_input('Number of Past Class Failures', min_value=0, max_value=10)
        Mjob = st.selectbox(
                'Mother\'s Job',
                options=[0, 1, 2, 3, 4],
                format_func=lambda x: {
                    4: 'Teacher',
                    1: 'Health care',
                    3: 'Services',
                    0: 'At home',
                    2: 'Other',
                }[x]
            )
        Medu = st.selectbox(
                'Mother\'s Education Level',
                options=[1, 2, 3, 4],
                format_func=lambda x: {
                    1: 'No formal education',
                    2: 'Some primary education',
                    3: 'Completed primary education',
                    4: 'Secondary education or higher',
                }[x]
            )

        internet = st.selectbox(
            'Internet Access',
            options=[0, 1],
            format_func=lambda x: {
                0: 'Yes',
                1: 'No',
            }[x]
        )
        Walc = st.selectbox(
            'Weekend Alcohol Consumption',
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: 'Very Low',
                2: 'Low',
                3: 'Medium',
                4: 'High',
                5: 'Very High',
            }[x]
        )


    if st.button("Predict"):
        # Convert inputs to correct format for the model
        input_data = pd.DataFrame({'studytime': [studytime],'reason': [reason],'higher': [higher],'traveltime': [traveltime],'Fedu': [Fedu],
            'Dalc': [Dalc],'age': [age],'failures': [failures],'Mjob': [Mjob],'Medu': [Medu],'internet': [internet],'Walc': [Walc]
        })

        # Make prediction
        prediction = model.predict(input_data)

        # Compute SHAP values
        shap_values = explainer(input_data)

        # Display the prediction
        st.markdown(f"<div class='col-md-6 card alert alert-success' style='color:black;width:300px;text-align:center'>Predicted Overall Score: {prediction[0]:.2f}</div>", unsafe_allow_html=True)

        # Display SHAP values
        st.write("Feature Impact Analysis:")
        for feature, impact in zip(input_data.columns, shap_values.values[0]):
            if impact > 0:
                st.markdown(f"<div style='color:green;'>The feature '{feature}' positively impacts the score by {impact:.2f}</div>", unsafe_allow_html=True)
            elif impact < 0:
                st.markdown(f"<div style='color:red;'>The feature '{feature}' negatively impacts the score by {impact:.2f}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='color:gray;'>The feature '{feature}' has no impact on the score.</div>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        feature_names = input_data.columns
        shap_values_means = shap_values.abs.mean(axis=0).values
        shap_values_df = pd.DataFrame({'Feature': feature_names, 'Impact': shap_values_means})
        shap_values_df = shap_values_df.sort_values(by='Impact', ascending=False)

        # Plotting
        ax.barh(shap_values_df['Feature'], shap_values_df['Impact'], color='blue')
        ax.set_xlabel('Mean Absolute SHAP Value')
        ax.set_title('Feature Impact Analysis')
        st.pyplot(fig)



          # Create a DataFrame for SHAP values
        impact_df = pd.DataFrame({
            'Feature': feature_names,
            'Impact': shap_values.values[0]
        })

        # Add bar chart
        st.bar_chart(impact_df.set_index('Feature'))

    

# Sidebar navigation
page = st.sidebar.selectbox("Select a page", ["Home", "Prediction Space", "About"])

if page == "Home":
    display_home_page()
elif page == "About":
    st.markdown("""
    <style>
    .about-container {
        font-family: Arial, sans-serif;
        line-height: 2.6;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .about-title {
        font-size: 2.5em;
        color: #333;
    }
    .about-text {
        font-size: 1.2em;
        color: #555;
    }
    </style>
    <div class="about-container">
        <h1 class="about-title">About This Application</h1>
        <p class="about-text">
            This GPA Prediction Platform uses advanced machine learning models to predict academic performance based on various factors. It helps students understand the impact of their academic behaviors and lifestyle choices on their overall grades.
        </p>
    </div>
    """, unsafe_allow_html=True)
elif page == "Prediction Space":
    process()
