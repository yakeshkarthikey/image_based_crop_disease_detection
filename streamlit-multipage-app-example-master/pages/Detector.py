import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
import time 
from skimage.io import imread,imsave
# st.title("Crop Disease Detector")
st.write("You have entered", st.session_state["my_input"])
x = st.session_state["my_input"]

print(x)
if x:
    def start(file,o):
        img_file_buffer = file
        image = Image.open(img_file_buffer)
        st.write("input image")
        # st.image(image)
        img_array = np.array(image) # if you want to pass it to OpenCV
        img = 'D:/Py/Bala_proj/color_img.jpg'
        imsave(img, img_array)
        # st.image(image, caption="The caption", use_column_width=True)
        # array = np.reshape(img_array, (128, 128))

        if file:
            st.info("file entered")
            st.image(file)

        button = st.button('Enter')
        

        if button:
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.1)
            my_bar.progress(percent_complete + 1, text=progress_text)
            if o=='Rice':
                model = load_model('D:/Py/Bala_proj/vgg16_rice.h5')
                batch_size = 16
                image = imread(img)
                img = Image.fromarray(image)
                img = img.resize((128, 128))
                img = np.array(img)
                input_img = np.expand_dims(img, axis=0)
                print(input_img)
                print(input_img.shape)
                i = input_img.reshape(-1,1)
                print("shape-i",i.shape)
                # result = model.predict_classes(input_img)
                result = model.predict(input_img)
                print(result)
                
                # st.write(result)
                st.subheader('The crop report is..')
                print(result)
                if result[0][0]:
                    st.subheader("Disease State: Rice_Brown_Spot")
                    st.write('''Description:
                                Brown spot is a fungal disease that infects the coleoptile, 
                                leaves, leaf sheath, panicle branches, glumes, and spikelets. Its most observable damage 
                                is the numerous big spots on the leaves which can kill the whole leaf. 
                                When infection occurs in the seed, unfilled grains or spotted or discolored seeds are formed.''')
                    st.header("Cause for the disease")
                    st.write('''Bipolaris oryzae is classified in the subdivision Deuteromycotina (imperfect fungi), 
                                class Deuteromycetes, order Moniliales, and family Dematiaceae and is the causal agent of brown 
                                spot disease of rice. Brown spot is one of the important rice diseases in the world.''')
                    st.header("Treatement to cure")
                    st.write('''Seed treatment with captan, thiram, chitosan, carbendazim, or mancozeb has been found to reduce seedling infection. 
                                Seed treatment with tricyclazole followed by spraying of mancozeb + tricyclazole at tillering and late booting stages gave good control of the disease.''')
                elif result[0][1]:
                    st.subheader("Disease state: Healthy state")
                        # st.write("......")
                        # st.header("Reason for the disease")
                        # st.write("......")
                        # st.header("Medicines to cure")
                        # st.write("......")
                elif result[0][2]:
                    st.subheader("Disease state: Leaf Blast")
                    st.write('''Description:
                                Rice blast caused by fungus Magnaporthe oryzae, is generally considered the most 
                                important disease of rice worldwide because of its extensive distribution and destructiveness under favourable conditions.''')
                    st.header("causes for the disease")
                    st.write('''This disease is caused by a fungus named Pyricularia orizae, which overwinters in rice seeds and infected rice stubble. The fungus reproductive structures, 
                                spores, can spread from these two sources to rice plants during the next growing season and initiate new infections.''')
                    st.header("Treatement to cure")
                    st.write('''Rice blast can be controlled by a combination of preventive measures and foliar fungicides 
                                applied when rice is in the late boot stage and again when it is 80 to 90 percent headed.''')

                        
            elif o=='Potato':
                model = load_model('D:/Py/Bala_proj/vgg16_p.h5')
                batch_size = 16
                image = imread(img)
                img = Image.fromarray(image)
                img = img.resize((128, 128))
                img = np.array(img)
                input_img = np.expand_dims(img, axis=0)
                print(input_img)
                print(input_img.shape)
                i = input_img.reshape(-1,1)
                print("shape-i",i.shape)
                    # result = model.predict_classes(input_img)
                result = model.predict(input_img)
                # st.write(result)
                st.subheader('The crop report is..')
                print(result)
                if result[0][0]:
                    st.subheader("Disease State: Early_Blight")
                    st.write('''Description:
                            Early blight is primarily a disease of stressed or senescing plants. Symptoms appear first on the oldest foliage. Affected leaves develop circular to angular dark brown lesions 0.12 to 0.16 inch (3–4 mm) in diameter. 
                            Concentric rings often form in lesions to produce characteristic target-board effect.''')
                    st.header("Reason for the disease")
                    st.write('''Early blight of potato is caused by the fungal pathogen Alternaria solani. The disease affects leaves, stems and tubers and can reduce yield, tuber size,
                            storability of tubers, quality of fresh-market and processing tubers and marketability of the crop.''')
                    st.header("Treatement to cure")
                    st.write('''Early blight can be minimized by maintaining optimum growing conditions, including proper fertilization, irrigation, and management of other pests. Grow later maturing, longer season varieties. 
                            Fungicide application is justified only when the disease is initiated early enough to cause economic loss.''')
                elif result[0][1]:
                    st.subheader("Disease state: Healthy")
                    # st.write("......")
                    # st.header("Reason for the disease")
                    # st.write("......")
                    # st.header("Medicines to cure")
                    # st.write("......")
                elif result[0][2]:
                    st.subheader("Disease state: Late Blight")
                    st.write('''Late blight caused by the fungus Phytophthora infestans is the most important disease of potato that can result into crop failures in a short period if appropriate
                            control measures are not adopted. Losses in potato yield can go as high as 80 percentage in epidemic years.''')
                    st.header("Reason for the disease")
                    st.write('''Late blight caused by the fungus Phytophthora infestans is the most important disease of potato that 
                            can result into crop failures in a short period if appropriate control measures are not adopted.''')
                    st.header("Treatement to cure")
                    st.write('''Late blight is controlled by eliminating cull piles and volunteer potatoes, using proper harvesting and storage practices,
                            and applying fungicides when necessary. Air drainage to facilitate the drying of foliage each day is important.''')
            
            elif o=='Maize':
                model = load_model('D:/Py/Bala_proj/vgg16_maize.h5')
                batch_size = 16
                image = imread(img)
                img = Image.fromarray(image)
                img = img.resize((128, 128))
                img = np.array(img)
                input_img = np.expand_dims(img, axis=0)
                print(input_img)
                print(input_img.shape)
                i = input_img.reshape(-1,1)
                print("shape-i",i.shape)
                    # result = model.predict_classes(input_img)
                result = model.predict(input_img)
                # st.write(result)
                st.subheader('The crop report is..')
                print(result)
                if result[0][0]:
                    st.subheader("Disease State: Blight")
                    st.write('''First symptoms on maize plants appear on the lower leaves. Spots that occur later, caused by spores distributed by wind, show on upper leaves. At the beginning of the infestation small, 
                            longish, watery stains arise which can grow into elongated bands of grey-green to light brown lesions.''')
                    st.header("Reason for the disease")
                    st.write('''Setosphaeria turcica/Exserohilum turcicum. There is a range of fungi that can cause leaf diseases in maize. The fungus,
                            causing by far the greatest damage in our climate, is called Setosphaeria turcica as teleomorph (sexual reproduction state).''')
                    st.header("Treatment to cure")
                    st.write('''Preventive Measures:
                                    -Plant resistant varieties if available in your area.
                                    -Plant different varieties of maize to avoid monocultures.
                                    -Make sure to keep field clean.
                                    -Rotate with non-host crops.
                                    -Plow deep to bury crop residues in the soil.
                                    -Plan a fallow after the harvest.''')
                elif result[0][1]:
                    st.subheader("Disease state: Common Rust")
                    st.write('''The common rust fungus overwinters in the southern U.S. and Mexico.
                            Urediniospores are blown north to the Midwestern Corn Belt in the summer and infection occurs in June or July.
                            Young leaves are most susceptible to infection and pustules are more likely to form after corn silking.''')
                    st.header("Reason for the disease")
                    st.write('''Common rust is caused by the fungus Puccinia sorghi and occurs every growing season. 
                            It is seldom a concern in hybrid corn. Rust pustules usually first appear in late June. 
                            Early symptoms of common rust are chlorotic flecks on the leaf surface.''')
                    st.header("Treatemet to cure")
                    st.write('''
                                    -Remove all infected parts and destroy them. For bramble fruits, remove and destroy all the infected plants and replant the area with resistant varieties.
                                    -Clean away all debris in between plants to prevent rust from spreading.
                                    -Avoid splashing water onto the leaves, as this can help spread rust.''')
                elif result[0][2]:
                    st.subheader("Disease state: Gray Leaf Spot")
                    st.write('''Gray leaf spot is typically the most serious foliar disease of corn in the U.S. corn belt,
                            although other diseases can be more important in areas and years where weather conditions do not favor gray leaf spot. 
                            Gray leaf spot requires extended periods of high humidity and warm conditions.''')
                    st.header("Reason for the disease")
                    st.write("Gray leaf spot is caused by the fungus Cercospora zeae-maydis.")
                    st.header("Medicines to cure")
                    st.write('''Fungicides. During the growing season, foliar fungicides can be used to manage gray leaf spot outbreaks. 
                            Farmers must consider the cost of the application and market value of their corn before determining if fungicides will be an economical solution to GLS.''')
                elif result[0][3]:
                    st.subheader(" Plant is in Healthy state")
                    # st.write("......")
                    # st.header("Reason for the disease")
                    # st.write("......")
                    # st.header("Medicines to cure")
                    # st.write("......")


    st.title("Crop Disease Detector")

    option = st.selectbox(
        'Enter the Crop Name',
        ("",'Maize', 'Potato', 'Rice'))

    st.write('You selected:', option)

    o = option
    print(o)
    st.write(o)
        # st.title("Crop Disease Detection ")
    st.subheader("Enter your Crop Image....")



    file = st.file_uploader("enter the image")


    try:
        start(file,o)
    except:
        pass
    