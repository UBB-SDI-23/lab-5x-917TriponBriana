import { Medication } from "./Medication";

export interface Dentist {
    id : number;
    dentist_first_name : string;
    dentist_last_name : string;
    dentist_age : number;
    dentist_country : string;
    dentist_salary : number;
    med : Medication[];
}