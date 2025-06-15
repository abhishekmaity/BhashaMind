import React from 'react';
import { render, screen } from '@testing-library/react';
import SummaryForm from '../SummarizerForm.js'; // Corrected import path

test('renders summary form input and button', () => {
  render(<SummaryForm />);
  expect(screen.getByPlaceholderText(/এখানে টেক্সট দিন/i)).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /সারাংশ তৈরি করুন/i })).toBeInTheDocument();
});
