//const PROD_BACKEND_API_URL = "ec2-16-170-108-25.eu-north-1.compute.amazonaws.com/app1/clin"; 
//https://dental-clinic-app.jumpingcrab.com/app1/clin
//const PROD_BACKEND_API_URL = "https://dental-clinic-app.mooo.com/app1/clin";
//http://ec2-16-170-164-154.eu-north-1.compute.amazonaws.com:8000/api/clin
// const PROD_BACKEND_API_URL = "/clinic";
const PROD_BACKEND_API_URL = "https://dental-clinic-app.mooo.com/clinic/";
const DEV_BACKEND_API_URL = "http://127.0.0.1:8000/clinic";

export const BACKEND_API_URL = 
    process.env.NODE_ENV === "development" ? DEV_BACKEND_API_URL : PROD_BACKEND_API_URL;

// export const BACKEND_API_URL = "https://dental-clinic-app.jumpingcrab.com/app1/clin/";