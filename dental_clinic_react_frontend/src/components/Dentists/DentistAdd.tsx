// import { useState } from "react";
// import { Link, useNavigate } from "react-router-dom"
// import { Dentist } from "../../models/Dentist";
// import { BACKEND_API_URL } from "../../constants";
// import axios from "axios";
// import { Button, Card, CardActions, CardContent, Container, IconButton, TextField } from "@mui/material";
// import ArrowBackIcon from "@mui/icons-material/ArrowBack";

// export const DentistAdd = () => {
//     const navigate = useNavigate();
//     const [dentist, setDentist] = useState<Dentist>({
//         dentist_first_name: "",
//         dentist_last_name: "",
//         dentist_age: 1,
//         dentist_country: "",
//         dentist_salary: 1,
//     });

//     const addDentist = async (event: {preventDefault: () => void}) => {
//         event.preventDefault();
//         try{
//             await axios.post(`${BACKEND_API_URL}/dentist`, dentist);
//             navigate("/dentist");
//         } catch (error) {
//             console.log(error);
//         }
//     };

//     return (
//         <Container>
//             <Card>
//                 <CardContent>
//                     <IconButton component={Link} sx = {{ mr:3 }} to={`/dentist`}>
//                         <ArrowBackIcon />
//                     </IconButton>{" "}
//                     <form onSubmit={addDentist}>
//                         <TextField
//                                 id="dentist_first_name"
//                                 label="First name"
//                                 variant="outlined"
//                                 fullWidth
//                                 sx={{ mb: 2 }}
//                                 onChange={(event) => setDentist({ ... dentist, dentist_first_name: event.target.value})}
//                         />
//                         <TextField
//                                 id="dentist_last_name"
//                                 label="Last name"
//                                 variant="outlined"
//                                 fullWidth
//                                 sx={{ mb: 2 }}
//                                 onChange={(event) => setDentist({ ... dentist, dentist_last_name: event.target.value})}
//                         />
//                         <TextField
//                                 id="dentist_age"
//                                 label="Age"
//                                 variant="outlined"
//                                 fullWidth
//                                 sx={{ mb: 2 }}
//                                 onChange={(event) => setDentist({ ... dentist, dentist_age: Number(event.target.value)})}
//                         />
//                         <TextField
//                                 id="dentist_country"
//                                 label="Country"
//                                 variant="outlined"
//                                 fullWidth
//                                 sx={{ mb: 2 }}
//                                 onChange={(event) => setDentist({ ... dentist, dentist_country: event.target.value})}
//                         />
//                         <TextField
//                                 id="dentist_salary"
//                                 label="Salary"
//                                 variant="outlined"
//                                 fullWidth
//                                 sx={{ mb: 2 }}
//                                 onChange={(event) => setDentist({ ... dentist, dentist_salary: Number(event.target.value)})}
//                         />

//                         <Button type="submit">Add Dentist</Button>
//                     </form>
//                 </CardContent>
//                 <CardActions></CardActions>
//             </Card>
//         </Container>
//     );
// }