// import {
// 	TableContainer,
// 	Paper,
// 	Table,
// 	TableHead,
// 	TableRow,
// 	TableCell,
// 	TableBody,
// 	CircularProgress,
// 	Container,
// 	IconButton,
// 	Tooltip,
// } from "@mui/material";
// import { useEffect, useState } from "react";
// import { Link } from "react-router-dom";
// import { Dentist } from "../../models/Dentist";
// import { BACKEND_API_URL } from "../../constants";
// import ReadMoreIcon from "@mui/icons-material/ReadMore";
// import EditIcon from "@mui/icons-material/Edit";
// import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
// import AddIcon from "@mui/icons-material/Add";

// export const DentistShowAll = () => {
//     const [loading, setLoading] = useState(false);
//     const [dentists, setDentists] = useState<Dentist[]>([]);

//     useEffect(() => {
// 		setLoading(true);
// 		fetch(`${BACKEND_API_URL}/dentist`)
// 			.then((response) => response.json())
// 			.then((data) => {
// 				setDentists(data);
// 				setLoading(false);
// 			});
// 	}, []);

//     console.log(dentists);

//     return(
//         <Container>
//             <h1>All Dentists</h1>

//             {loading && <CircularProgress />}
//             {!loading && dentists.length === 0 && <p>No dentists found!</p>}
//             {!loading && (
//                 <IconButton component={Link} sx={{ mr: 3}} to={`/dentist/add`}>
//                     <Tooltip title="Add a new dentist!" arrow>
//                         <AddIcon color="primary" />
//                     </Tooltip>
//                 </IconButton>
//             )}
//             {!loading && dentists.length > 0 && (
//                 <TableContainer component={Paper}>
//                     <Table sx={{minWidth: 650}} aria-label="simple table">
//                         <TableHead>
//                             <TableRow>
//                                 <TableCell>#</TableCell>
//                                 <TableCell align="right">First Name</TableCell>
//                                 <TableCell align="right">Last Name</TableCell>
//                                 <TableCell align="right">Age</TableCell>
//                                 <TableCell align="right">Country</TableCell>
//                                 <TableCell align="right">Salary</TableCell>
//                             </TableRow>
//                         </TableHead>
//                         <TableBody>
//                             {dentists.map((dentist, index) => (
//                                 <TableRow key={dentist.id}>
//                                     <TableCell component="th" scope="row">
//                                         {index + 1}
//                                     </TableCell>
//                                     <TableCell component="th" scope="row">
//                                         <Link to={`/dentist/${dentist.id}/`} title="View dentist details.">
//                                             {dentist.dentist_first_name}
//                                         </Link>
//                                     </TableCell>
//                                     <TableCell align="right">{dentist.dentist_last_name}</TableCell>
//                                     <TableCell align="right">{dentist.dentist_age}</TableCell>
//                                     <TableCell align="right">{dentist.dentist_country}</TableCell>
//                                     <TableCell align="right">{dentist.dentist_salary}</TableCell>
//                                     <TableCell align="right">
//                                         <IconButton
//                                                 component={Link}
//                                                 sx={{ mr: 3}}
//                                                 to={`/dentist/${dentist.id}/`}>
//                                                 <Tooltip title="View dentist details." arrow>
//                                                         <ReadMoreIcon color="primary" />
//                                                 </Tooltip>
//                                         </IconButton>

//                                         <IconButton component={Link} sx={{ mr: 3}} to={`/dentist/${dentist.id}/edit`}>
//                                             <EditIcon />
//                                         </IconButton>

//                                         <IconButton component={Link} sx={{ mr: 3 }} to={`/dentist/${dentist.id}/delete`}>
//                                             <DeleteForeverIcon sx={{ color: "red"}} />
//                                         </IconButton>
//                                     </TableCell>
//                                 </TableRow>
//                             ))}
//                         </TableBody>
//                     </Table>
//                 </TableContainer>
//             )}
//         </Container>
//     );
// };