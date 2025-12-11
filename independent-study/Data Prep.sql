-- Create the table
create
or replace table student_info (
    first_name varchar(25),
    last_name varchar(25),
    email varchar(25),
    course varchar(10),
    work_date date,
    time_in varchar(15),
    time_out varchar(15),
    work_type varchar(25)
);
-- Create the file format to read in the data
create file format csv_frmt type = CSV,
skip_header = 1,
field_delimiter = ',',
trim_space = TRUE;

-- Copy the file into the table
COPY INTO student_info
from
    @indep_study.public.files files = ('genData.csv') file_format = (format_name = csv);

-- Check    
select
    *
from
    student_info;