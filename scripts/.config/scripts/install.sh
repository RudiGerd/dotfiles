#!/bin/bash

# Set the filename for the CSV file
csvfile="packages.csv"

# Initialize an array to store the package names
packages=()

# Read in the package names from the CSV file
while IFS=',' read -r package
do
  packages+=("$package")
done < "$csvfile"

# Initialize an array to store the failures
failures=()

# Install each package and track any failures
for package in "${packages[@]}"
do
  echo "Installing $package..."
  sudo pacman -S --noconfirm "$package"
  if [ $? -ne 0 ]; then
    failures+=("$package, could not be installed")
  fi
done

# Print the installation summary
echo "Installation summary:"

if [ ${#failures[@]} -eq 0 ]; then
  echo "All packages were installed successfully!"
else
  echo "The following packages could not be installed:"
  for failure in "${failures[@]}"
  do
    echo "$failure"
  done
fi
