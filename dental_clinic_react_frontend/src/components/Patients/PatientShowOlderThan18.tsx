import { useEffect, useState } from "react";
import { BACKEND_API_URL } from "../../constants";
import { CircularProgress, Container, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from "@mui/material";
import { PatientStatistic } from "../../models/PatientStatistic";

export const PatientShowOlderThan18 = () => {
    const [loading, setLoading] = useState(true);
    const [patients, setPatients] = useState([]);

    useEffect(() => {
        fetch(`${BACKEND_API_URL}/patient/older-than-18/`)
            .then(response => response.json())
            .then(data => {
                setPatients(data);
                setLoading(false);
            }
            );
    }, []);

    console.log(patients);

    return (
        <Container>
            <h1>All Patients Who Are Older Than 18</h1>
            {loading && <CircularProgress />}
            
            {!loading && patients.length == 0 && <div>No patients were found!</div>}

            {!loading && patients.length > 0 && (
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 900}} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>#</TableCell>
                                <TableCell align="center">First Name</TableCell>
                                <TableCell align="center">Last Name</TableCell>
                                <TableCell align="center">Age</TableCell>
                                <TableCell align="center">Country</TableCell>
                                <TableCell align="center">Consultation</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {patients.map((patient:PatientStatistic, index) => (
                                <TableRow key={patient.id}>
                                    <TableCell component="th" scope="row">
                                        {index + 1}
                                    </TableCell>
                                    <TableCell align="center">{patient.patient_first_name}</TableCell>
                                    <TableCell align="center">{patient.patient_last_name}</TableCell>
                                    <TableCell align="center">{patient.patient_age}</TableCell>
                                    <TableCell align="center">{patient.patient_country}</TableCell>
                                    <TableCell align="center">{patient.patient_consultation}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            )}
        </Container>
    )
}