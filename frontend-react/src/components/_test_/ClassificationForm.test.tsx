import React from 'react';
import { render, screen } from '@testing-library/react';
import ClassificationForm from '../ClassifierForm.js';

test('renders classification form input and button', () => {
  render(<ClassificationForm />);
  expect(screen.getByPlaceholderText(/এখানে টেক্সট দিন/i)).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /শ্রেণিবিন্যাস করুন/i })).toBeInTheDocument();
});
