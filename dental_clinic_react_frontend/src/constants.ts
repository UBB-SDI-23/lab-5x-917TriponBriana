//const PROD_BACKEND_API_URL = "ec2-16-170-108-25.eu-north-1.compute.amazonaws.com/app1/clin";
const PROD_BACKEND_API_URL = "http://ec2-16-170-133-56.eu-north-1.compute.amazonaws.com/app1/clin";
const DEV_BACKEND_API_URL = "http://127.0.0.1:8000/app1/clin";

export const BACKEND_API_URL = 
    process.env.NODE_ENV === "development" ? DEV_BACKEND_API_URL : PROD_BACKEND_API_URL;

// export const BACKEND_API_URL = "https://dental-clinic-deploy-frontend.netlify.app/";