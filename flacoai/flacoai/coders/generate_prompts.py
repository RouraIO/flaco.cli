"""Prompts for SwiftUI code generation."""

from .base_prompts import CoderPrompts


class GeneratePrompts(CoderPrompts):
    """Prompts for generating SwiftUI code from templates."""

    main_system = """You are an expert SwiftUI developer and code generator.

Your role is to generate high-quality SwiftUI views based on templates and user requirements.

When generating code:
1. Use modern SwiftUI best practices (iOS 15+)
2. Follow Apple's Human Interface Guidelines
3. Write clean, readable code with proper spacing
4. Include helpful comments for TODO items
5. Use SF Symbols for icons
6. Implement proper state management with @State, @Binding
7. Add accessibility labels where appropriate
8. Include #Preview for easier development

Template Variables:
- Always ask the user if required template variables are missing
- Suggest sensible defaults when appropriate
- Allow customization of variable values

Code Quality:
- Generated code should compile without errors
- Use type-safe APIs (no force unwrapping unless necessary)
- Follow Swift naming conventions (camelCase for properties, PascalCase for types)
- Keep view bodies focused and extract complex logic to private methods

You have access to these SwiftUI template types:
- login: Login view with email/password fields
- settings: Settings view with toggles and navigation
- list: List view with search, add, and delete functionality
- detail: Detail view for displaying item information
- tabview: TabView with 4 customizable tabs

For each template, you'll need to provide specific variables.
The template engine will handle substitution automatically.
"""

    example_messages = [
        dict(
            role="user",
            content="Generate a login view for MyWeatherApp",
        ),
        dict(
            role="assistant",
            content="""I'll generate a login view for MyWeatherApp using the login template.

This will create a SwiftUI view with:
- Email and password fields
- Login button with loading state
- Error message display
- Forgot password link
- Sign up navigation

The template uses these variables:
- VIEW_NAME: LoginView
- APP_NAME: MyWeatherApp

Here's the generated code:

```swift
import SwiftUI

struct LoginView: View {
    @State private var email: String = ""
    @State private var password: String = ""
    @State private var isLoading: Bool = false
    @State private var errorMessage: String?

    var body: some View {
        NavigationView {
            VStack(spacing: 20) {
                // Logo or header
                Text("MyWeatherApp")
                    .font(.largeTitle)
                    .fontWeight(.bold)
                    .padding(.bottom, 40)

                // Email field
                TextField("Email", text: $email)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .textContentType(.emailAddress)
                    .autocapitalization(.none)
                    .keyboardType(.emailAddress)

                // Password field
                SecureField("Password", text: $password)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .textContentType(.password)

                // Error message
                if let errorMessage = errorMessage {
                    Text(errorMessage)
                        .foregroundColor(.red)
                        .font(.caption)
                }

                // Login button
                Button(action: {
                    handleLogin()
                }) {
                    if isLoading {
                        ProgressView()
                            .progressViewStyle(CircularProgressViewStyle(tint: .white))
                    } else {
                        Text("Log In")
                            .fontWeight(.semibold)
                    }
                }
                .frame(maxWidth: .infinity)
                .frame(height: 50)
                .background(Color.accentColor)
                .foregroundColor(.white)
                .cornerRadius(10)
                .disabled(isLoading || email.isEmpty || password.isEmpty)

                // Forgot password link
                Button("Forgot Password?") {
                    // Handle forgot password
                }
                .font(.caption)
                .foregroundColor(.accentColor)

                Spacer()

                // Sign up link
                HStack {
                    Text("Don't have an account?")
                        .foregroundColor(.gray)
                    Button("Sign Up") {
                        // Handle sign up navigation
                    }
                    .foregroundColor(.accentColor)
                }
                .font(.caption)
            }
            .padding()
            .navigationTitle("Welcome")
        }
    }

    private func handleLogin() {
        isLoading = true
        errorMessage = nil

        // TODO: Implement authentication logic
        // Example:
        // Task {
        //     do {
        //         try await AuthService.shared.login(email: email, password: password)
        //         // Navigate to main app
        //     } catch {
        //         errorMessage = error.localizedDescription
        //     }
        //     isLoading = false
        // }

        // Placeholder - remove when implementing real auth
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            isLoading = false
        }
    }
}

#Preview {
    LoginView()
}
```

You can now:
1. Copy this code to your Xcode project
2. Customize the TODO sections for your authentication logic
3. Adjust styling to match your app's design
4. Add additional fields if needed (e.g., remember me checkbox)
""",
        ),
    ]
