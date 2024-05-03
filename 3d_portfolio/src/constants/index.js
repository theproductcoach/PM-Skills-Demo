import {
    mobile,
    backend,
    creator,
    web,
    javascript,
    typescript,
    html,
    css,
    reactjs,
    redux,
    tailwind,
    nodejs,
    mongodb,
    git,
    figma,
    docker,
    meta,
    starbucks,
    tesla,
    shopify,
    tanda,
    vision6,
    productcoach,
    citrusad,
    ladbrokes, 
    carrent,
    jobit,
    tripguide,
    threejs,
    openai,
  } from "../assets";
  
  export const navLinks = [
    {
      id: "about",
      title: "About",
    },
    {
      id: "work",
      title: "Work",
    },
    {
      id: "contact",
      title: "Contact",
    },
  ];
  
  const services = [
    {
      title: "Product Leader",
      icon: web,
    },
    {
      title: "Product Coach",
      icon: mobile,
    },
    {
      title: "Product Mentor",
      icon: backend,
    },
    {
      title: "Content Creator",
      icon: creator,
    },
  ];
  
  const technologies = [
    {
      name: "HTML 5",
      icon: html,
    },
    {
      name: "CSS 3",
      icon: css,
    },
    {
      name: "JavaScript",
      icon: javascript,
    },
    {
      name: "TypeScript",
      icon: typescript,
    },
    {
      name: "React JS",
      icon: reactjs,
    },
    {
      name: "Redux Toolkit",
      icon: redux,
    },
    {
      name: "Tailwind CSS",
      icon: tailwind,
    },
    {
      name: "Node JS",
      icon: nodejs,
    },
    {
      name: "MongoDB",
      icon: mongodb,
    },
    {
      name: "Three JS",
      icon: threejs,
    },
    {
      name: "git",
      icon: git,
    },
    {
      name: "figma",
      icon: figma,
    },
    {
      name: "docker",
      icon: docker,
    },
    {
      name: "openai",
      icon: openai,
    },
  ];
  
  const experiences = [
    {
      title: "Product Management Coach",
      company_name: "The Product Coach",
      company_url: "https://productcoach.io",
      icon: productcoach,
      iconBg: "#383E56",
      date: "April 2023 - Present",
      points: [
        "Launched a bespoke Product Management coaching service providing customised mentorship for individuals and corporate clients.",
        "Developed the ProductOps Playbook using extensive industry knowledge to create a scalable product management operational framework.",
        "Established a comprehensive Product Manager role at a fintech startup, overseeing role definition and recruitment, culminating in a top-tier hire.",
        "Co-hosted a Product Tank event to enhance awareness and accessibility of the APM role and pathways into Product Management.",
      ],
    },
    {
      title: "Group Product Manager",
      company_name: "Tanda",
      company_url: "https://tanda.co",
      icon: tanda,
      iconBg: "#E6DEDD",
      date: "October  2021 - June 2023",
      points: [
        "Pioneered the industry’s first templated legal document solution with a leading law firm, enhancing onboarding efficiency and introducing a new modular pricing model.",
        "Delivered an automated break compliance solution, significantly reducing liability risks and achieving a 90% adoption rate, leading to a record-breaking $3 million contract.",
        "Streamlined roster validation across platforms, boosting operational efficiency and enhancing usability and compliance.",
        "Developed a global Product Management team, accelerating leadership development through personalised coaching and the successful launch of an Associate Product Manager program.",
      ],
    },
    {
      title: "Senior Product Manager",
      company_name: "Vision6",
      company_url: "https://vision6.com.au/",
      icon: vision6,
      iconBg: "#383E56",
      date: "March 2021 - October 2021",
      points: [
        "Managed a team of five engineers and a designer, fostering development through effective coaching and best practice application.",
        "Launched a new email template editor that cut email creation time by 20%, streamlining marketing efforts",
        "Enhanced customer feedback mechanisms within products by implementing FullStory to capture direct user interactions",
        "Developed an enterprise pricing and go-to-market strategy focused on large security-sensitive customers.",
      ],
    },
    {
      title: "Senior Product Manager",
      company_name: "CitrusAd",
      company_url: "https://citrusad.com/",
      icon: citrusad,
      iconBg: "#E6DEDD",
      date: "March 2019 - December 2020",
      points: [
        "Secured a major partnership with a top US retail group through strategic negotiations and scalable, innovative solutions.",
        "Strengthened ties with leading Australian grocers, negotiating renewals and a three-year, $3 million professional services agreement.",
        "Expanded operations post a $6.5 million Series A round, securing partnerships with top-tier retailers including Groupon, Sainsbury's, Tesco, and Petco.",
        "Hired and managed two Product Managers, enhancing product development and streamlining workflows, significantly contributing to robust MRR growth.",
      ],
    },
    {
      title: "Product Manager",
      company_name: "Ladbrokes",
      company_url: "https:ladbrokes.com.au",
      icon: ladbrokes,
      iconBg: "#383E56",
      date: "March 2016 - August 2018",
      points: [
        "Launched Same Game Multi after a tech stack overhaul, generating $350,000 in its first week with high profit margins.",
        "Developed the State of Origin early pay-out promotion in collaboration with multiple teams, boosting revenue for a bet type from $800,000 to $1.8 million year-on-year.",
        "Implemented NBA Live Streaming across three platforms for over 1300 games, enhancing service by adopting scaled Agile practices with a ThoughtWorks coach.",
        "Mentored three Product Managers in Agile methods and served as an escalation point for service-related issues, ensuring consistency and efficiency.",
      ],
    },
  ];
  
  const testimonials = [
    {
      testimonial:
        "I thought it was impossible to make a website as beautiful as our product, but Rick proved me wrong.",
      name: "Sara Lee",
      designation: "CFO",
      company: "Acme Co",
      image: "https://randomuser.me/api/portraits/women/4.jpg",
    },
    {
      testimonial:
        "I've never met a web developer who truly cares about their clients' success like Rick does.",
      name: "Chris Brown",
      designation: "COO",
      company: "DEF Corp",
      image: "https://randomuser.me/api/portraits/men/5.jpg",
    },
    {
      testimonial:
        "After Rick optimized our website, our traffic increased by 50%. We can't thank them enough!",
      name: "Lisa Wang",
      designation: "CTO",
      company: "456 Enterprises",
      image: "https://randomuser.me/api/portraits/women/6.jpg",
    },
  ];
  
  const projects = [
    {
      name: "Car Rent",
      description:
        "Web-based platform that allows users to search, book, and manage car rentals from various providers, providing a convenient and efficient solution for transportation needs.",
      tags: [
        {
          name: "react",
          color: "blue-text-gradient",
        },
        {
          name: "mongodb",
          color: "green-text-gradient",
        },
        {
          name: "tailwind",
          color: "pink-text-gradient",
        },
      ],
      image: carrent,
      source_code_link: "https://github.com/",
    },
    {
      name: "Job IT",
      description:
        "Web application that enables users to search for job openings, view estimated salary ranges for positions, and locate available jobs based on their current location.",
      tags: [
        {
          name: "react",
          color: "blue-text-gradient",
        },
        {
          name: "restapi",
          color: "green-text-gradient",
        },
        {
          name: "scss",
          color: "pink-text-gradient",
        },
      ],
      image: jobit,
      source_code_link: "https://github.com/",
    },
    {
      name: "Trip Guide",
      description:
        "A comprehensive travel booking platform that allows users to book flights, hotels, and rental cars, and offers curated recommendations for popular destinations.",
      tags: [
        {
          name: "nextjs",
          color: "blue-text-gradient",
        },
        {
          name: "supabase",
          color: "green-text-gradient",
        },
        {
          name: "css",
          color: "pink-text-gradient",
        },
      ],
      image: tripguide,
      source_code_link: "https://github.com/",
    },
  ];
  
  export { services, technologies, experiences, testimonials, projects };