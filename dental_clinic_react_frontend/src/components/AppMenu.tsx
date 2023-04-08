
import { Link, useLocation } from "react-router-dom";
import SchoolIcon from "@mui/icons-material/School";
import LocalLibraryIcon from "@mui/icons-material/LocalLibrary";
import { Box, AppBar, Toolbar, IconButton, Typography, Button } from "@mui/material";


export const AppMenu = () => {
    const location = useLocation();
    const path = location.pathname;

    return (
        <Box sx={{ flexGrow: 1}}>
                <AppBar position="static" sx={{marginBottom: "20px"}}>
                    <Toolbar>
                        <IconButton
                            component={Link}
                            to="/"
                            size="large"
                            edge="start"
                            color="inherit"
                            aria-label="school"
                            sx={{ mr: 2 }}>
                            <SchoolIcon/>    
                        </IconButton>
                        <Typography variant="h6" component="div" sx={{mr: 5}}>
                            Patients management
                        </Typography>
                        <Button
                            variant={path.startsWith("/patient") ? "outlined": "text"}
                            to="/patient"
                            component={Link}
                            color="inherit"
                            sx={{mr: 5}}
                            startIcon={<LocalLibraryIcon />}>
                                Patients
                        </Button>

                        <Button
                            variant={path.startsWith("/patient") ? "outlined": "text"}
                            to="/patient/older-than-18"
                            component={Link}
                            color="inherit"
                            sx={{ mr: 5 }}
                            startIcon={<LocalLibraryIcon />}>
                                Patients Older Than 18
                            </Button>
                    </Toolbar>
                </AppBar>
        </Box>
                
    );
};