import { Dentist } from "./Dentist";

export interface Medication {
    id : number;
    med_name : string;
    med_active_subst : string;
    med_price : number;
    med_expiration_date : string;
    med_usage : string;
    dent : Dentist[];
}