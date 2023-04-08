import {
	TableContainer,
	Paper,
	Table,
	TableHead,
	TableRow,
	TableCell,
	TableBody,
	CircularProgress,
	Container,
	IconButton,
	Tooltip,
    Button,
} from "@mui/material";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import { Patient } from "../../models/Patient";

export const PatientShowAll = () => {
    const [loading, setLoading] = useState(false);
    const [patients, setPatients] = useState<Patient[]>([]);

    useEffect(() => {
		setLoading(true);
		fetch(`${BACKEND_API_URL}/patient`)
			.then((response) => response.json())
			.then((data) => {
				setPatients(data);
				setLoading(false);
			});
	}, []);

    console.log(patients);

    const sortPatient = () => {
        const sortedPatients = [ ...patients].sort((first: Patient, second: Patient) => {
            if (first.patient_age < second.patient_age){
                return -1;
            }
            if (first.patient_age > second.patient_age){
                return 1;
            }
            return 0;
        })
        console.log(sortedPatients);
        setPatients(sortedPatients);
    }

    return(
        <Container>
            <h1>All Patients</h1>

            {loading && <CircularProgress />}
            {!loading && patients.length === 0 && <p>No patients found!</p>}
            {!loading && (
                <IconButton component={Link} sx={{ mr: 3}} to={`/patient/add`}>
                    <Tooltip title="Add a new patient!" arrow>
                        <AddIcon color="primary" />
                    </Tooltip>
                </IconButton>
            )}

            {!loading && (
                <Button sx={{color: "blue"}} onClick={sortPatient}>
                    Sort Patients
                </Button>
            )}

            {!loading && patients.length > 0 && (
                <TableContainer component={Paper}>
                    <Table sx={{minWidth: 650}} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>#</TableCell>
                                <TableCell align="right">First Name</TableCell>
                                <TableCell align="right">Last Name</TableCell>
                                <TableCell align="right">Age</TableCell>
                                <TableCell align="right">Country</TableCell>
                                <TableCell align="right">Consultation</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {patients.map((patient, index) => (
                                <TableRow key={patient.id}>
                                    <TableCell component="th" scope="row">
                                        {index + 1}
                                    </TableCell>
                                    <TableCell component="th" scope="row">
                                        <Link to={`/patient/${patient.id}/`} title="View patient details.">
                                            {patient.patient_first_name}
                                        </Link>
                                    </TableCell>
                                    <TableCell align="right">{patient.patient_last_name}</TableCell>
                                    <TableCell align="right">{patient.patient_age}</TableCell>
                                    <TableCell align="right">{patient.patient_country}</TableCell>
                                    <TableCell align="right">{patient.patient_consultation}</TableCell>
                                    <TableCell align="right">
                                        <IconButton
                                                component={Link}
                                                sx={{ mr: 3}}
                                                to={`/patient/${patient.id}/`}>
                                                <Tooltip title="View patient details." arrow>
                                                        <ReadMoreIcon color="primary" />
                                                </Tooltip>
                                        </IconButton>

                                        <IconButton component={Link} sx={{ mr: 3}} to={`/patient/${patient.id}/edit`}>
                                            <EditIcon />
                                        </IconButton>

                                        <IconButton component={Link} sx={{ mr: 3 }} to={`/patient/${patient.id}/delete`}>
                                            <DeleteForeverIcon sx={{ color: "red"}} />
                                        </IconButton>
                                    </TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            )}
        </Container>
    );
};