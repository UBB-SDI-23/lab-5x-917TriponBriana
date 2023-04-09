import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom"
import { Patient } from "../../models/Patient";
import { BACKEND_API_URL } from "../../constants";
import { Box, Card, CardActions, CardContent, Container, IconButton } from "@mui/material";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import { PatientFull } from "../../models/PatientFull";

export const PatientDetail = () => {
    const {patientId} = useParams();
    const [patient, setPatient] = useState<Patient>();

    useEffect(() => {
        const fetchPatient =async () => {
            const response = await fetch(`${BACKEND_API_URL}/patient/${patientId}/`);
            const patient = await response.json();
            setPatient(patient);
            console.log(patient);
        };
        fetchPatient();
    }, [patientId]);

    return (
        <Container>
        <Card>
            <CardContent>
                <IconButton component={Link} sx={{ mr: 3 }} to={`/patient`}>
                    <ArrowBackIcon />
                </IconButton>{" "}
                <h1 style={{textAlign:"center"}}>Patient Details</h1>
                <p style={{textAlign:"left"}}>First Name: {patient?.patient_first_name}</p>
                <p style={{textAlign:"left"}}>Last Name: {patient?.patient_last_name}</p>
                <p style={{textAlign:"left"}}>Age: {patient?.patient_age}</p>
                <p style={{textAlign:"left"}}>Country: {patient?.patient_country}</p>
                <p style={{textAlign:"left"}}>Consultation: {patient?.patient_consultation}</p>
            </CardContent>
            <CardActions>
                <IconButton component={Link} sx={{ mr: 3 }} to={`/patient/${patientId}/edit`}>
                    <EditIcon />
                </IconButton>

                <IconButton component={Link} sx={{ mr: 3 }} to={`/patient/${patientId}/delete`}>
                    <DeleteForeverIcon sx={{ color: "red" }} />
                </IconButton>
            </CardActions>
        </Card>
    </Container>
    );
};
