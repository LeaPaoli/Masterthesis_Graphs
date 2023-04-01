########################################################################################################################
## READ ME
########################################################################################################################
"""
This Code replicates figures 2 and 3 of my Master's thesis.

Please be sure to download the folder "Data" before executing the run.


Data Sources:
 - CBDC Tracker. (2022). Today’s Central Bank Digital Currencies Status. Retrieved February
    5, 2023, from https://cbdctracker.org/.
 - Fis. (2022). The Global Payments Report. Retrieved February 4, 2023, from
    https://worldpay.globalpaymentsreport.com/en

Author:
Lea Katharina Paoli
"""
########################################################################################################################
## PACKAGES
########################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import os

# Style Adjustments for Matplotlib
plt.style.use('grayscale')
plt.rcParams["figure.facecolor"] = "white" # Back Background white
plt.rcParams["font.family"] = "Times New Roman" # change font
plt.rcParams.update({'font.size': 12}) # change font size

########################################################################################################################
## SET RELATIVE PATHS
########################################################################################################################
cwd = os.getcwd()
print(f"This is your current working directory: {cwd}")


out = cwd + "\\Out\\"
CBDC_data = cwd + "\\Data\\CBDCTracker.xlsx"
ecom_data = cwd + "\\Data\\ecom.xlsx"
pos_data = cwd + "\\Data\\pos.xlsx"

# Check whether out folder has been created, yet.
if not os.path.exists(out):
    # if not: create it
    os.makedirs(out)

########################################################################################################################
## FUNCTIONS
########################################################################################################################
def calculate_yearly_occurances():
    """
        Calculates the yearly occurances of different statuses in a dataframe.

        Returns:
        myresults (list): list of cumulative occurances for each year
        myresults_cancelled (list): list of cancelled occurances for each year
        myresults_pilot (list): list of pilot occurances for each year
        myresults_research (list): list of research occurances for each year
        myresults_poc (list): list of proof of concept occurances for each year
        myresults_launched (list): list of launched occurances for each year

    """
    # list of years
    myyears = list(df["year"].unique())
    myyears.sort()
    myresults = []
    myresults_cancelled = []
    myresults_pilot = []
    myresults_research = []
    myresults_poc = []
    myresults_launched = []
    for y in myyears:
        #print(y)
        a = (len(df[(df["year"] == y) & (df["status"] == "Cancelled")]))
        b = (len(df[(df["year"] == y) & (df["status"] == "Pilot")]))
        c = (len(df[(df["year"] == y) & (df["status"] == "Research")]))
        d = (len(df[(df["year"] == y) & (df["status"] == "Proof of concept")]))
        e = (len(df[(df["year"] == y) & (df["status"] == "Launched")]))
        myresult = b + c + d + e - a
        myresults.append(myresult)
        myresults_cancelled.append(a)
        myresults_pilot.append(b)
        myresults_research.append(c)
        myresults_poc.append(d)
        myresults_launched.append(e)
    return myresults, myresults_cancelled, myresults_pilot, myresults_research, myresults_poc, myresults_launched

def calculate_yearly_cum_occurances():
    """
        Calculates the yearly occurances of different statuses in a dataframe.

        Returns:
        myresults (list): list of cumulative occurances for each year
        myresults_cancelled (list): list of cancelled occurances for each year
        myresults_pilot (list): list of pilot occurances for each year
        myresults_research (list): list of research occurances for each year
        myresults_poc (list): list of proof of concept occurances for each year
        myresults_launched (list): list of launched occurances for each year

    """
    # list of years
    myyears = list(df["year"].unique())
    myyears.sort()
    myresults_cancelled = []
    myresults_pilot = []
    myresults_research = []
    myresults_poc = []
    myresults_launched = []
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for y in myyears:
        a = a + (len(df[(df["year"] == y) & (df["status"] == "Cancelled")]))
        b = b + (len(df[(df["year"] == y) & (df["status"] == "Pilot")]))
        c = c + (len(df[(df["year"] == y) & (df["status"] == "Research")]))
        d = d + (len(df[(df["year"] == y) & (df["status"] == "Proof of concept")]))
        e = e + (len(df[(df["year"] == y) & (df["status"] == "Launched")]))
        myresults_cancelled.append(a)
        myresults_pilot.append(b)
        myresults_research.append(c)
        myresults_poc.append(d)
        myresults_launched.append(e)
    return myresults_cancelled, myresults_pilot, myresults_research, myresults_poc, myresults_launched


def zip_yearly_occurances():
    """
        This function calculates the yearly occurrences of different statuses for each year
        in a given dataframe 'df'. It returns a pandas dataframe with the columns:
        "year", "cum. occur.", "Cancelled", "Pilot", "Research", "Proof of Concept", and "Launched".

        Returns:
        df_zipped: a pandas dataframe with 7 columns: "year","Cancelled",
        "Pilot", "Research", "Proof of Concept", and "Launched".
    """
    result1, result2, result3, result4, result5, result6 = calculate_yearly_occurances()
    # list of years
    myyears = list(df["year"].unique())
    myyears.sort()

    # zip lists into one dataframe
    zipped = list(zip(myyears, result1, result2, result3, result4, result5, result6))

    # Pandas Dataframe
    df_zipped = pd.DataFrame(zipped, columns=["year", "cum. occur.", "Cancelled", "Pilot", "Research", "Proof of Concept", "Launched"])
    return df_zipped

def zip_yearly_cum():
    """
        This function calculates the cumulative occurrences of different statuses for each year
        in a given dataframe 'df'. It returns a pandas dataframe with the columns:
        "year", "cum. occur.", "Cancelled", "Pilot", "Research", "Proof of Concept", and "Launched".

        Returns:
        df_zipped: a pandas dataframe with 7 columns: "year","Cancelled",
        "Pilot", "Research", "Proof of Concept", and "Launched".
    """
    result1, result2, result3, result4, result5 = calculate_yearly_cum_occurances()
    # list of years
    myyears = list(df["year"].unique())
    myyears.sort()
    #print(myyears)

    # zip lists into one dataframe
    zipped = list(zip(myyears, result1, result2, result3, result4, result5))

    # Pandas Dataframe
    df_zipped_cum = pd.DataFrame(zipped, columns=["year", "Cancelled", "Pilot", "Research", "Proof of Concept", "Launched"])
    return df_zipped_cum

def zip_short():
    """
            This function calculates the cumulative occurrences of different statuses for each year
            in a given dataframe 'df'. It returns a pandas dataframe with the columns:
            "year", "Cancelled", "Pilot", "Research", "Proof of Concept", and "Launched".

            Returns:
            df_zipped: a pandas dataframe with 6 columns: "year","Cancelled",
            "Pilot", "Research", "Proof of Concept", and "Launched".
        """
    result1, result2, result3, result4, result5, result6 = calculate_yearly_occurances()
    # list of years
    myyears = list(df["year"].unique())
    myyears.sort()
    # print(myyears)

    # zip lists into one dataframe
    zipped = list(zip(myyears, result2, result3, result4, result5, result6))

    # Pandas Dataframe
    df_zipped_short = pd.DataFrame(zipped, columns=["year", "Cancelled", "Pilot", "Research", "Proof of Concept", "Launched"])
    return df_zipped_short


### Functions for plotting
def plot_yearly_occurances(df_zipped_cum):
    """
        This function takes the zipped dataframe as input and plots all 5 results as a line graph.
        Figure is saved in folder "Out".


        Args:
        df_zipped: a pandas dataframe with the columns: "year", "cum. occur.", "Cancelled",
        "Pilot", "Research", "Proof of Concept", and "Launched".

        Returns:
        fig
    """
    fig, ax = plt.subplots()
    df_zipped_cum = df_zipped_cum[df_zipped_cum["year"] >= 2005]
    ax.plot(df_zipped_cum["year"], df_zipped_cum["Cancelled"], label="Cancelled")
    ax.plot(df_zipped_cum["year"], df_zipped_cum["Pilot"], label="Pilot")
    ax.plot(df_zipped_cum["year"], df_zipped_cum["Research"], label="Research")
    ax.plot(df_zipped_cum["year"], df_zipped_cum["Proof of Concept"], label="Proof of Concept", linestyle='dashed')
    ax.plot(df_zipped_cum["year"], df_zipped_cum["Launched"], label="Launched", linestyle='dashed')

    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Projects")
    ax.legend()
    plt.show()
    return fig


def save_df_as_table_image(df,
                           filename,
                           col_labels=None,
                           fontsize=8,
                           no_decimals=True):
    """
    This function takes a pandas dataframe and saves it as an image of a table.

    Args:
        df (pandas.DataFrame): the dataframe to be saved as an image of a table.
        filename (str): the name of the file to be saved.
        col_labels (list): a list of strings representing the new column names.
        fontsize (int): the font size of the text in the table.
        no_decimals (bool): a flag to indicate whether or not to show decimal points in the figure.
    """
    # Check if new column names were provided
    if col_labels is not None:
        df.columns = col_labels

    # Round the values in the dataframe if no_decimals is True
    if no_decimals:
        df = df.round(0).astype(int)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Hide the axes
    ax.axis('off')

    # Create the table
    table = ax.table(cellText=df.values, colLabels=df.columns,  loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)
    table.scale(1, 1.5)

    # Save the figure as an image
    filename = "{}{}".format(out, filename)
    fig.savefig(filename)


def two_pie_charts(df_pos, df_ecom):
    """
        This function plots two pie charts next to each other

        Args:
        df_pos: a pandas dataframe with the columns: "Means of Payment" and "Percentage".
        df_ecom: a pandas dataframe with the columns: "Means of Payment" and "Percentage".

        Returns:
        fig
    """
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    for i, df in enumerate([df_pos, df_ecom]):
        # Create labels with percentages
        labels = [f"{row['Means of Payment']} ({row['Percentage']:.0f}%)" for _, row in df.iterrows()]

        # Plot pie chart
        patches, texts, autotexts = axs[i].pie(df['Percentage'], labels=labels, textprops={'fontsize': 9},
                                               startangle=-35, labeldistance=1.1, autopct='')

        # Set label font size and position
        for text in texts:
            text.set_fontsize(9)
        for autotext in autotexts:
            autotext.set_fontsize(9)
            autotext.set_color('black')
            autotext.set_position((-1.2, 0))

        # Set title and remove percentage from the pie chart
        axs[i].set_title("Means of Payment at Point of Sale" if i == 0 else "Means of Payment in E-Commerce")
        plt.setp(autotexts, visible=False)

    # Remove the gray background
    fig.patch.set_facecolor('white')

    # Adjust the spacing between the two subplots
    plt.subplots_adjust(wspace=0.35)

    # Display
    plt.show(block=False)
    plt.pause(1)  # Pause for 3 seconds to make sure the figure is shown

    return fig


########################################################################################################################
## Import and Clean CBDC dataset
########################################################################################################################

df = pd.read_excel(CBDC_data)

# rename columns
df.rename(columns = {"Digital currency":"name", "Country / Region": "region", "Central Bank(s)":"CB", "Announcement Year":"year", "Update rate":"update", "Retail/Wholesale":"type", "Status":"status"}, inplace = True )

# drop if "status" is missing
df = df.dropna(subset=["status", "year"])

print("HEAD (renamed):")
pd.set_option('display.max_columns', None) # show all columns in header
print(df.head())

# Drop if Wholesale CBDC
df = df[df.type != "Wholesale"]

# Rename "Retail,Wholsesale" into "Retail"
df = df.replace("Retail,Wholesale","Retail")

# Drop unnecessary columns
df = df.drop(["region", "CB", "update"], axis=1, inplace=False)

print("After modifications:")
print(df.head())

# count occurrences overall
occur = df.groupby(["status"]).size()
print("Occurances overall")
print(occur)

# count occurrences of status per year
occur = df.groupby(["year", "status"]).size()
print("Occurances yearly")
print(occur)

df_plt = zip_yearly_occurances()
print(df_plt)

# Drop if year smaller than 2013 (only data for > 2014)
df_plt = df_plt[df_plt['year'] >= 2013]

print("min date")
print(df_plt['year'].min())

########################################################################################################################
## Import Ecom / POS Datasets
########################################################################################################################
df_ecom = pd.read_excel(ecom_data)
print(df_ecom.head())
df_ecom.info()

df_pos = pd.read_excel(pos_data)
print(df_pos.head())
df_pos.info()

########################################################################################################################
## Call Graph Plotting Functions
########################################################################################################################
df_zipped = zip_yearly_occurances() # input of consecutive functions
df_zipped_short = zip_short() # input of consecutive functions
df_zipped_cumulative = zip_yearly_cum()

print(df_zipped_short)
save_df_as_table_image(df_zipped_short, "table.png", col_labels=None, no_decimals=True)

fig = plot_yearly_occurances(df_zipped_cumulative)
fig.savefig("{}{}".format(out, "plot_all_occur.png"), dpi=600)

# Define a list of grayscale colors excluding black
colors = [(0.7, 0.7, 0.7), (0.5, 0.5, 0.5), (0.3, 0.3, 0.3), (0.9, 0.9, 0.9), (0.6, 0.6, 0.6)]

# Set the custom color scheme as the default color cycle for Matplotlib
plt.rcParams["axes.prop_cycle"] = plt.cycler("color", colors)

fig = two_pie_charts(df_ecom, df_pos)
fig.savefig("{}{}".format(out, "piecharts.png"), dpi=600)

print("end of file.")