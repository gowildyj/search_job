def save_to_file(file_name,jobs):
  f = open(f"{file_name}.csv","w",encoding = "utf=8")
  f.write("position, company, location, URL\n")
  
  for job in jobs:
    f.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
  
  f.close()