library(rvest)
library(tidyverse)
library(dplyr)

existing_data <- read.csv("Candidates.csv", sep = ";", stringsAsFactors = FALSE)
filtered_data <- existing_data %>%
  filter(Winner == "Yes" & House != "Lok Sabha") %>%
  select(-Winner, -House, -Comment)

write.csv(filtered_data,"Filtered_MLAs.csv")


link <- "https://www.myneta.info/state_assembly.php?state="
states <- c("Andhra Pradesh","Arunachal%20Pradesh", "Assam", "Bihar", 
            "Chattisgarh", "Delhi", "Goa", "Gujarat", 
            "Haryana", "Himachal Pradesh", "Jammu And Kashmir", "Jharkhand",
            "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
            "Manipur", "Meghalaya", "Mizoram", "Nagaland",
            "Odisha", "Puducherry", "Punjab", "Rajasthan",
            "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
            "Uttarakhand", "Uttar Pradesh", "West Bengal")

states <- gsub(" ", "%20", states)
states <- paste(link, states, sep = "")

# Function to extract links containing the word "winner"
extract_winner_links <- function(url) {
  html <- read_html(url)
  links <- html %>% html_elements("a")
  winner_links <- links %>% 
    html_attr("href") %>% 
    keep(~grepl("winner", .)) %>%
    paste(url, ., sep = "")
  transformed_links <- winner_links %>% 
    str_replace("https://www.myneta.info/state_assembly.php\\?state=.*?/", "") %>% 
    str_replace("index.php\\?action=show_winners&sort=default", "index.php?action=summary&subAction=winner_serious_crime&sort=candidate#summary")
  return(transformed_links)
}

all_winner_links <- lapply(states, extract_winner_links)
all_winner_links <- unlist(all_winner_links)
all_winner_links <- paste("https://www.myneta.info/", all_winner_links, sep="")

write.csv(all_winner_links,"links.csv")
