import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Sidebar menu
st.sidebar.title('Navigation')

page = st.sidebar.selectbox(
    'Choose a Page',
    ['Introduction', 'Picture Display', 'Data Visualization']
)

# Introduction
if page == 'Introduction':
    st.title('Data Visualization App')

    st.write(
        'Welcome to my simple Streamlit application. '
        'This app demonstrates basic data visualization '
        'using Streamlit, Pandas, and Matplotlib.'
    )

    st.subheader('Features')
    st.write('• Picture display using a button')
    st.write('• Bar chart visualization')
    st.write('• Interactive slider')
    st.write('• Interactive checkbox')


# Picture Display
elif page == 'Picture Display':
    st.title('Picture Display')

    st.write('Click the button below to display an image.')

    if st.button('Show Picture'):
        st.image(
            'https://commons.wikimedia.org/wiki/Special:Redirect/file/Berries_(USDA_ARS).jpg',
        caption='Fresh Berries',
        use_container_width=True
        )


# Data Visualization
elif page == 'Data Visualization':
    st.title('Data Visualization')

    st.write('Use the slider to modify the fruit quantities.')

    # Interactive sliders
    strawberry_quantity = st.slider(
        'Number of Strawberries',
        min_value=1,
        max_value=50,
        value=10
    )

    blueberry_quantity = st.slider(
        'Number of Blueberries',
        min_value=1,
        max_value=50,
        value=15
    )

    raspberry_quantity = st.slider(
        'Number of Raspberries',
        min_value=1,
        max_value=50,
        value=7
    )

    # Data
    data = {
        'Fruits': ['Strawberry', 'Blueberry', 'Raspberry'],
        'Quantities': [
            strawberry_quantity,
            blueberry_quantity,
            raspberry_quantity
        ]
    }

    df = pd.DataFrame(data)

    # Checkbox
    show_data = st.checkbox('Show Data Table')

    if show_data:
        st.dataframe(df)

    # Button
    if st.button('Show Bar Chart'):

        fig, ax = plt.subplots()

        ax.bar(
            df['Fruits'],
            df['Quantities'],
            color='pink'
        )

        ax.set_xlabel('Fruits')
        ax.set_ylabel('Quantities')
        ax.set_title('Fruit Quantities')

        st.pyplot(fig)
