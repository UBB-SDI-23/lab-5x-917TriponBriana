import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom"
import { BACKEND_API_URL } from "../../constants";
import axios from "axios";
import { Button, Card, CardActions, CardContent, Container, IconButton, TextField } from "@mui/material";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";

export const PatientUpdate = () => {
    const navigate = useNavigate();
    const {patientId} = useParams();

    const [loading, setLoading] = useState(true);
    const [patient, setPatient] = useState({
        patient_first_name: "",
        patient_last_name:"",
        patient_age:1,
        patient_country:"",
        patient_consultation:"",
    });

    useEffect(() => {
        const fetchPatient = async () => {
            const respose = await fetch(`${BACKEND_API_URL}/patient/${patientId}/`);
            const patient = await respose.json();
            setPatient({
                patient_first_name: patient.patient_first_name,
                patient_last_name: patient.patient_first_name,
                patient_age: patient.patient_age,
                patient_country: patient.patient_country,
                patient_consultation: patient.patient_consultation
            })
            setLoading(false);
            console.log(patient);
        };
        fetchPatient();
    }, [patientId]);

    const updatePatient =async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        try {
            await axios.put(`${BACKEND_API_URL}/patient/${patientId}/`, patient);
            navigate(`/tennisplayers/${patientId}`);
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <Container>
            <Card>
                <CardContent>
                    <IconButton component={Link} sx={{ mr: 3}} to={`/patient`}>
                        <ArrowBackIcon />
                    </IconButton>{" "}
                    <form onSubmit={updatePatient}>
						<TextField
							id="patient_first_name"
							label="First name"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setPatient({ ...patient, patient_first_name: event.target.value })}
						/>
						<TextField
							id="patient_last_name"
							label="Last name"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setPatient({ ...patient, patient_last_name: event.target.value })}
						/>

                        <TextField
							id="patient_age"
							label="Age"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setPatient({ ...patient, patient_age: Number(event.target.value) })}
						/>

                        <TextField
							id="patient_country"
							label="Country"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setPatient({ ...patient, patient_country: event.target.value })}
						/>

                        <TextField
							id="patient_consultation"
							label="Consultation"
							variant="outlined"
							fullWidth
							sx={{ mb: 2 }}
							onChange={(event) => setPatient({ ...patient, patient_consultation: event.target.value })}
						/>
                        <Button type="submit">Update Patient</Button>
                    </form>
                </CardContent>
                <CardActions></CardActions>
            </Card>
        </Container>
    )
};