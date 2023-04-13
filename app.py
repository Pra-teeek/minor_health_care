import streamlit as st

# Set up the page title and header
st.title("Healthcare Management System")

# Create a navigation menu
menu_items = ["pain_disease", "Itching",
              "Fever", "bleeding", "Stomach", "Eyes"]
menu_selection = st.sidebar.selectbox("Select a page", menu_items)

if menu_selection == "pain_disease":
    st.write("A migraine can cause severe throbbing pain or a pulsing sensation, usually on one side of the head. It's often accompanied by nausea, vomiting, and extreme sensitivity to light and sound. Migraine attacks can last for hours to days, and the pain can be so severe that it interferes with your daily activities.")
    # Add code for patient information management

    # Sample output to show patient information
    show_patients = st.button("Show patients")
    if show_patients:
        st.subheader("More symptoms")
        patients = ["joint_pain", "stomach_pain", "pain_behind_the_eyes", "back_pain", "abdominal_pain", "chest_pain", "pain_during_bowel_movements",
                    "pain_in_anal_region", "neck_pain", "knee_pain", "hip_joint_pain", "muscle_pain", "belly_pain", "painful_walking"]

        for patient in patients:
            if patient == "joint_pain":
                joint_pain_radio = st.radio(patient, ("Yes", "No"))
                if joint_pain_radio == "Yes":
                    st.subheader("Symptoms")
                    precautions = []
                    precautions.append(
                        "Okay. From how many days?: " + st.text_input("From how many days?"))
                    precautions.append("Are you experiencing any joint pain?: " +
                                       st.text_input("Are you experiencing any joint pain?"))
                    precautions.append(
                        "Are you experiencing vomiting?: " + st.text_input("Are you experiencing vomiting?"))
                    precautions.append(
                        "Are you experiencing fatigue?: " + st.text_input("Are you experiencing fatigue?"))
                    precautions.append("Are you experiencing yellowish skin?: " +
                                       st.text_input("Are you experiencing yellowish skin?"))
                    precautions.append("Are you experiencing dark urine?: " +
                                       st.text_input("Are you experiencing dark urine?"))
                    precautions.append(
                        "Are you experiencing nausea?: " + st.text_input("Are you experiencing nausea?"))
                    precautions.append("Are you experiencing loss of appetite?: " +
                                       st.text_input("Are you experiencing loss of appetite?"))
                    precautions.append("Are you experiencing abdominal pain?: " +
                                       st.text_input("Are you experiencing abdominal pain?"))
                    precautions.append("Are you experiencing yellowing of eyes?: " +
                                       st.text_input("Are you experiencing yellowing of eyes?"))
                    for precaution in precautions:
                        st.write(precaution)
                    pre = "You should take the consultation from doctor.You may have  Hepatitis DHepatitis D, also known as the hepatitis delta virus, is an infection that causes the liver to become inflamed. This swelling can impair liver function and cause long-term liver problems, including liver scarring and cancer. The condition is caused by the hepatitis D virus(HDV)"
                    st.write(pre)


elif menu_selection == "Itching":
    st.write("Itching is an unpleasant sensation that compels a person to scratch the affected area. Itching can be caused by various factors, such as skin conditions, allergies, and infections.")
    # Add code for patient information management

    # Sample output to show patient information
    show_patients = st.button("Show patients")
    if show_patients:
        st.subheader("More symptoms")
        patients = ["itching", "internal_itching"]
        for patient in patients:
             if patient == "itching":
                itching_radio = st.radio(patient, ("Yes", "No"))
                if itching_radio == "Yes":
                    st.subheader("Symptoms")
                    pro ="You should take the consultation from doctor.ou may have  Drug Reaction or  Chronic cholestasisAn adverse drug reaction (ADR) is an injury caused by taking medication. ADRs may occur following a single dose or prolonged administration of a drug or result from the combination of two or more drugs.Chronic cholestatic diseases, whether occurring in infancy, childhood or adulthood, are characterized by defective bile acid transport from the liver to the intestine, which is caused by primary damage to the biliary epithelium in most cases"
                    st.write(pro)
                    

elif menu_selection == "Fever":
    st.write("Fever is a common symptom of many medical conditions. It can be caused by infections, inflammation, or other underlying conditions.")
    # Add code for patient information management

    # Sample output to show patient information
    show_patients = st.button("Show patients")
    if show_patients:
        st.subheader("More symptoms")
        patients = ["high_fever", "mild_fever"]
        for patient in patients:
            if patient == "high_fever":
                itching_radio = st.radio(patient, ("Yes", "No"))
                if itching_radio == "Yes":
                    st.subheader("Symptoms")
                    list = ["From how many days ? : 12",
"Are you experiencing any" 
,"muscle_weakness ? : yes"
,"stiff_neck ? : yes"
,"swelling_joints ? : yes"
,"movement_stiffness ? : yes",
"painful_walking ? : yes"]
                    for lis in list:
                        st.write(lis)
                    pr1 ="You should take the consultation from doctor. You may have  Arthritis Arthritis is the swelling and tenderness of one or more of your joints. The main symptoms of arthritis are joint pain and stiffness, which typically worsen with age. The most common types of arthritis are osteoarthritis and rheumatoid arthritis."
                    st.write(pr1)
            st.write(patient)
            pr2 =" YOU SHOULD TAKE FOLLOWING SOME MEASURE:   Take following measures : 1 ) exercise 2  ) use hot and cold therapy 3  ) try acupuncture 4  ) massage"
            st.write(pr2)
elif menu_selection == "bleeding":
    st.write("Bleeding can occur for many reasons, including injury, surgery, or medical conditions such as hemorrhoids or ulcerative colitis.")
    
    show_patients = st.button("Show patients")
    if show_patients:
        st.subheader("More symptoms")
        patients = ["stomach bleeding"]
        for patient in patients:
            if patient == "stomach bleeding":
                itching_radio = st.radio(patient, ("Yes", "No"))
                if itching_radio == "Yes":
                    st.subheader("Symptoms")

                    pr1 ="It might not be that bad but you should take precautions.You may have  Hepatitis EA rare form of liver inflammation caused by infection with the hepatitis E virus (HEV). It is transmitted via food or drink handled by an infected person or through infected water supplies in areas where fecal matter may get into the water. Hepatitis E does not cause chronic liver disease."
                    st.write(pr1)
            st.write(patient)
            pr2 =" YOU SHOULD TAKE FOLLOWING SOME MEASURE:   Take following measures : stop alcohol consumption2 ) rest3 ) consult doctor4 ) medication"
            st.write(pr2)# Add code for patient information management

    # Sample output to show patient information
