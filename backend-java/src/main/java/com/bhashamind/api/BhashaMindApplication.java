package com.bhashamind.api;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.SpringApplication;

/**
 * Main application class for BhashaMind API.
 */
@SpringBootApplication
public final class BhashaMindApplication {

	/**
	 * Private constructor to prevent instantiation as a utility class.
	 */
	private BhashaMindApplication() {
		// Utility classes should not have a public or default constructor.
	}

	/**
	 * Main entry point for the Spring Boot application.
	 * @param args Command line arguments.
	 */
	public static void main(String[] args) {
		SpringApplication.run(BhashaMindApplication.class, args);
	}
}
