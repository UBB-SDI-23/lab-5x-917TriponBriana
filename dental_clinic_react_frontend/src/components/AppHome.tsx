import { Container, CssBaseline, Typography } from "@mui/material"
import React from "react"

export const AppHome = () => {
    return (
        <React.Fragment>
            <CssBaseline />

            <Container maxWidth="xl">
                <Typography variant="h1" component="h1" gutterBottom>
                    Welcome!
                </Typography>
            </Container>
        </React.Fragment>
    );
};